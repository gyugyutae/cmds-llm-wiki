from pathlib import Path

import fitz
from PIL import Image, ImageDraw, ImageFont, ImageOps


DESKTOP = Path("/mnt/c/Users/user/Desktop")
WIKI = DESKTOP / "cmds-llm-wiki"
WORK = DESKTOP / "GNU-UNLV_활동실적_작업본"
OUTPUT = DESKTOP / "GNU-UNLV_AI-창업_관련활동실적_김규태.pdf"

PAGE_W = 1488
PAGE_H = 2105
MARGIN = 72
GAP = 48
FONT_BOLD = Path("/mnt/c/Windows/Fonts/NotoSansKR-Bold.ttf")


def open_rgb(path: Path) -> Image.Image:
	with Image.open(path) as image:
		return ImageOps.exif_transpose(image).convert("RGB")


def fit(image: Image.Image, max_w: int, max_h: int) -> Image.Image:
	scale = min(max_w / image.width, max_h / image.height)
	width = max(1, round(image.width * scale))
	height = max(1, round(image.height * scale))
	return image.resize((width, height), Image.Resampling.LANCZOS)


def single_page(path: Path) -> Image.Image:
	canvas = Image.new("RGB", (PAGE_W, PAGE_H), "white")
	image = fit(open_rgb(path), PAGE_W - 2 * MARGIN, PAGE_H - 2 * MARGIN)
	x = (PAGE_W - image.width) // 2
	y = (PAGE_H - image.height) // 2
	canvas.paste(image, (x, y))
	return canvas


def pdf_page(path: Path, page_number: int = 0) -> Image.Image:
	doc = fitz.open(path)
	page = doc.load_page(page_number)
	pixmap = page.get_pixmap(matrix=fitz.Matrix(4, 4), alpha=False)
	image = Image.frombytes("RGB", (pixmap.width, pixmap.height), pixmap.samples)
	doc.close()
	return image


def pdf_single_page(path: Path, page_number: int = 0) -> Image.Image:
	canvas = Image.new("RGB", (PAGE_W, PAGE_H), "white")
	image = fit(pdf_page(path, page_number), PAGE_W - 2 * MARGIN, PAGE_H - 2 * MARGIN)
	x = (PAGE_W - image.width) // 2
	y = (PAGE_H - image.height) // 2
	canvas.paste(image, (x, y))
	return canvas


def stacked_page(paths: list[Path], crops: dict[int, tuple[int, int, int, int]] | None = None) -> Image.Image:
	crops = crops or {}
	images = []
	for index, path in enumerate(paths):
		image = open_rgb(path)
		if index in crops:
			image = image.crop(crops[index])
		images.append(image)

	available_h = PAGE_H - 2 * MARGIN - GAP * (len(images) - 1)
	cell_h = available_h // len(images)
	images = [fit(image, PAGE_W - 2 * MARGIN, cell_h) for image in images]

	canvas = Image.new("RGB", (PAGE_W, PAGE_H), "white")
	total_h = sum(image.height for image in images) + GAP * (len(images) - 1)
	y = (PAGE_H - total_h) // 2
	for image in images:
		x = (PAGE_W - image.width) // 2
		canvas.paste(image, (x, y))
		y += image.height + GAP
	return canvas


def labeled_stacked_page(
	label: str,
	paths: list[Path],
	crops: dict[int, tuple[int, int, int, int]] | None = None,
) -> Image.Image:
	crops = crops or {}
	font = ImageFont.truetype(str(FONT_BOLD), 48)
	heading_h = 105
	images = []
	for index, path in enumerate(paths):
		image = open_rgb(path)
		if index in crops:
			image = image.crop(crops[index])
		images.append(image)

	available_h = PAGE_H - 2 * MARGIN - heading_h - GAP * (len(images) - 1)
	cell_h = available_h // len(images)
	images = [fit(image, PAGE_W - 2 * MARGIN, cell_h) for image in images]

	canvas = Image.new("RGB", (PAGE_W, PAGE_H), "white")
	draw = ImageDraw.Draw(canvas)
	box = draw.textbbox((0, 0), label, font=font)
	text_w = box[2] - box[0]
	draw.text(((PAGE_W - text_w) // 2, MARGIN), label, fill="black", font=font)

	total_h = sum(image.height for image in images) + GAP * (len(images) - 1)
	y = MARGIN + heading_h + (PAGE_H - MARGIN - heading_h - total_h) // 2
	for image in images:
		x = (PAGE_W - image.width) // 2
		canvas.paste(image, (x, y))
		y += image.height + GAP
	return canvas


def write_pdf(pages: list[Image.Image]) -> None:
	doc = fitz.open()
	for index, page_image in enumerate(pages, start=1):
		page_path = WORK / f"page-{index:02d}.jpg"
		page_image.save(page_path, "JPEG", quality=78, optimize=True, progressive=True, subsampling=2)
		page = doc.new_page(width=595.276, height=841.89)
		page.insert_image(page.rect, filename=str(page_path), keep_proportion=False)
	doc.set_metadata({
		"title": "GNU-UNLV AI·창업 관련 활동실적",
		"author": "김규태",
		"subject": "AI·창업 등 관련 활동 실적 1부",
	})
	OUTPUT.unlink(missing_ok=True)
	doc.save(OUTPUT, garbage=4, deflate=True)
	doc.close()


def main() -> None:
	WORK.mkdir(parents=True, exist_ok=True)
	pages = [
		single_page(DESKTOP / "2026 경남권 대학생 창업동아리 창업역량강화 심화교육 대상.png"),
		single_page(DESKTOP / "2026  GNU 개척리더스 창업 아이디어톤 경진대회 최우수상.png"),
		single_page(WORK / "u300-award.png"),
		single_page(DESKTOP / "스크린샷_21-9-2026_175841_u300.kr.jpeg"),
		single_page(WIKI / "80. References/Attachments/2026-01-24-FPT-Vietnam-AI-Completion-Certificate.jpeg"),
		labeled_stacked_page(
			"모두의 창업 1차·2차 지원",
			[
				DESKTOP / "스크린샷_21-9-2026_155739_www.modoo.or.kr.jpeg",
				DESKTOP / "스크린샷_21-9-2026_155845_play.google.com.jpeg",
			],
			crops={1: (0, 105, 909, 701)},
		),
		single_page(WORK / "gnu-buddy.png"),
		single_page(WIKI / "80. References/Attachments/TMU-2026-Record-of-Study.jpg"),
		single_page(WIKI / "80. References/Attachments/TMU-Global-Leadership-100-Hours-Certificate.jpg"),
		single_page(WIKI / "80. References/Attachments/TMU-UN-SDG-Solutions-Day-Certificate.jpg"),
		pdf_single_page(DESKTOP / "창업에듀수료증 (3).pdf"),
		single_page(DESKTOP / "스크린샷_21-9-2026_155647_www.threads.com.jpeg"),
	]
	write_pdf(pages)
	print(OUTPUT)


if __name__ == "__main__":
	main()
