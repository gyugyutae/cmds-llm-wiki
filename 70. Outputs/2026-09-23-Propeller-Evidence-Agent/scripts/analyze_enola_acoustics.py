"""Read-only exploratory ENOLA pressure analysis; not a calibrated test certificate.

Usage: python3 analyze_enola_acoustics.py path/to/acoustics/*.csv
Requires numpy and scipy. No source files are modified.
Protocol is a team proposal, not a reproduction of the authors' processing.
"""
import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from scipy.signal import periodogram, welch


def metrics(t, p):
    if len(t) < 8192 or not np.isfinite(t).all() or not np.isfinite(p).all():
        raise ValueError('Too short or nonfinite samples')
    dt = np.diff(t)
    if np.any(dt <= 0) or not np.allclose(dt, np.median(dt), rtol=1e-4, atol=0):
        raise ValueError('Time samples must be increasing and approximately uniform')
    fs = 1 / np.mean(dt)
    if fs / 2 < 10000:
        raise ValueError('Nyquist below chosen analysis upper bound')
    p = p - p.mean()
    ms = np.mean(p ** 2)
    if ms <= 0:
        raise ValueError('Zero pressure variance')
    # Full rectangular periodogram integral must match time-domain variance.
    fp, pp = periodogram(p, fs, window='boxcar', detrend=False, scaling='density')
    assert np.isclose(np.sum(pp) * (fp[1] - fp[0]), ms, rtol=1e-10)
    f, psd = welch(p, fs, window='hann', nperseg=8192, noverlap=4096,
                   nfft=8192, detrend=False, scaling='density', average='mean')
    # Small tolerance accommodates decimal timestamp rounding.
    mask = (f >= 100 - 0.001) & (f <= 10000 + 0.001)
    band_ms = np.sum(psd[mask]) * (f[1] - f[0])
    return dict(samples=len(p), duration_seconds=len(p)/fs, fs_hz=fs,
                unweighted_whole_file_db=10*np.log10(ms/(20e-6)**2),
                unweighted_band_db=10*np.log10(band_ms/(20e-6)**2),
                requested_band_hz=[100,10000],
                included_bin_centers_hz=[float(f[mask][0]),float(f[mask][-1])],
                welch=dict(window='hann',nperseg=8192,noverlap=4096,nfft=8192),
                reference_pressure_pa=20e-6,
                status='exploratory; microphone mapping/calibration/repeatability not verified')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('files', nargs='*', type=Path)
    parser.add_argument('--self-test', action='store_true')
    args = parser.parse_args()
    if args.self_test:
        t = np.arange(131072)/65536
        result = metrics(t, np.sqrt(2)*np.sin(2*np.pi*1000*t))
        expected = 20*np.log10(1/20e-6)
        assert abs(result['unweighted_band_db']-expected) < 1e-6
        assert abs(result['unweighted_whole_file_db']-expected) < 1e-6
        print('PASS: known 1 Pa RMS sine and Parseval cross-check')
    for path in args.files:
        raw = path.read_bytes()
        if raw.splitlines()[0].decode().strip() != 'index,time[s],pressure[Pa]':
            raise ValueError(f'Unexpected units/header: {path}')
        a = np.loadtxt(path, delimiter=',', skiprows=1)
        result = metrics(a[:,1], a[:,2])
        result.update(file=path.name, sha256=hashlib.sha256(raw).hexdigest())
        print(json.dumps(result, ensure_ascii=False))


if __name__ == '__main__':
    main()
