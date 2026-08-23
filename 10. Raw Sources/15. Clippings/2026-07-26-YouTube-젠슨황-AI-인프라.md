---
type: raw-source
aliases:
  - 인공지능 1타강사 젠슨황 선생님
  - 젠슨 황 AI 인프라 설명
description: "Translated YouTube interview transcript presenting Jensen Huang's framing of AI factories, token generation, accelerated computing, and enterprise AI infrastructure."
author:
  - "BZCF | 비즈까페"
date created: 2026-07-26
date modified: 2026-07-26
date ingested: 2026-07-26
tags:
  - raw-source
  - clippings
  - ai-infrastructure
  - accelerated-computing
  - nvidia
source: "https://www.youtube.com/watch?v=_w8iKUfU9s4"
sourcePublished: 2026-06-22
clippedAt: 2026-07-25
category: "Clippings"
status: ingested
collectionPurpose: "취업/포트폴리오 및 독서/책/학습 — AI를 챗봇 기능이 아니라 연산 인프라·AI 팩토리·토큰 생산 체계로 이해하고 반도체 및 시스템 관점의 개발자 커리어 탐색에 활용하기 위해 수집."
mainVaultRelated: []
mainVaultCmds: ""
---

# 젠슨 황의 AI 인프라 설명

## Source Notes

- Capture method: Obsidian Web Clipper transcript of a translated YouTube upload.
- Attribution boundary: Jensen Huang is the interview speaker; BZCF uploaded/translated the captured version.
- Verification boundary: translation and excerpt context were not checked against an original event transcript.
- Compiled use: [[AI 팩토리와 토큰 생산 인프라]], [[AI 시대의 개발자 학습 전략]], and [[김규태 Career Narrative]].

---

## Original Content
![](https://www.youtube.com/watch?v=_w8iKUfU9s4)

15분 남짓한 시간 안에 많은 것들이 담겨있습니다. 이렇게 핸드폰으로, 컴퓨터로 멋진 통찰들 즐길 수 있음에 감사합니다. 오늘도 수고하셨습니다.  
  
Translated by J  
  
DISCLAIMER  
\- The copyright of the original video belongs to the original copyright holder.  
\- We check the copyright permission through the YouTube system, and if it is not confirmed within the system, we proceed with the translation work in the process of seeking permission through separate e-mails.  
\- The Korean subtitles of the video were added within the scope of not distorting the contents of the original video in order to share the valuable video with more Korean viewers.  
\- The purpose of this video is ONLY for the public good, such as education, motivation, or sharing of ideas with a wider public, and is not used for any additional purpose. In particular, there is NO revenue generated through YouTube AT ALL.  
\- If you(copyright holder) request deletion, removal, correction, etc in any reasons caused by uploading the video, please contact us at 'businessnewsdaily@naver.com' and we will make corrections accordingly.

## Transcript

**0:00** · We are in the middle of a massive AI revolution. It is probably bigger and faster than even the Industrial Revolution.

**0:09** · And you have called out what's happening right now as the largest infrastructure build-out in human history. At the center of that build-out is the AI factory. And the company enabling all of that is Nvidia. Can you tell us what is an AI factory and why is it the best investment for any enterprise in the next decade? Okay, so Um you could you could understand AI in a in a particular number of ways. The the way that you understand AI probably most is through a chatbot, through a web browser, uh you're interacting with it, you give it a prompt, it say something back to you.

**0:38** · And and even those of you who have been using AI for some time, uh you've seen in the last couple two three years a very significant evolution, improvement in the capabilities of AI.

**0:48** · Two years ago, you heard about ChatGPT.

**0:51** · And ChatGPT basically is a computer software that understands the input you give it. It can perceive, understand information, and it can translate and generate the information into something else. Okay, so you can give it a prompt and you can say, "Here's this PDF I gave you. Um I would like you now to summarize it." It went from text to text. You could also tell it, "Here's a PDF I gave you. Um I would like you to now generate an image of that story." It go text to image. You could use go from image to text, meaning you could give it a picture and you can "What's happening inside this picture?" It goes text uh image to text. Does that make sense?

**1:24** · Anything to anything else. And AI in the last in two years time two years ago was largely able to do this translation. We call it generation, generative models, okay? Generative AI. But the the thing that is very big deal inside that word generative AI is in order to do something even more valuable than generation, understanding and generating, is thinking. Well, you can't think if you don't generate words. And so the the foundation of generative AI gave us the ability to generate internal thoughts, thinking, reasoning, step-by-step reasoning, problem-solving.

**1:57** · It also allowed us to do another thing that is now very important, which is generate intelligence to control something else. To generate control to use a tool. Does that make sense? To use a browser, use a spreadsheet, use Photoshop, use PowerPoint, use something, use AutoCAD, use another tool.

**2:12** · Now, that tool today is digital, but someday that tool will be mechanical.

**2:17** · So, if I generate a command to a mechanical system, that would be called robotics. If I generate commands for uh a machine with steering wheel, that would be called self-driving cars. Does that make sense? Okay. And so, 2 years ago, 2 years ago, in fact, you saw the foundations, we call it ChatGPT, and everybody said, "Uh, you know, it's fun, it's it's silly, or it produced a whole bunch of crazy hallucinated text."

**2:36** · That's all true, but it was the foundational technology that led to all of this. 2 years later, we now have agentic systems. Now, that's one view of AI. I just described the view, which is what can AI do, right? And so, now all of you realize, you see it from ChatGPT, you see it from Codex, you see it from Cloud Code, you see you see that it's now able to not just understand, but it's able to do work. Reason and do work.

**2:58** · Now, 2 years ago, when AI was able to understand you and generate information, that was interesting, novel, a little cute, whenever you need a poem written, great way to do it, right? Who doesn't want to write a country song? And so, so that was 2 years ago, but now, because it's able to do work, AI is valuable. Valuable meaning it can generate information, it can generate useful work, and it could be paid for it. Because we pay for we're we're interested in having friends that are smart, we love people who are know-it-alls, but we don't pay them for it. We pay for people who do work. Does that make sense? All right.

**3:28** · Which is what happened in the last 2 years, AI went from having this capability to now agentic went from not use not very valuable to now producing useful work.

**3:38** · So much useful work that you and I are doing this every day. We're paying AI by the hour, right? And so, we might pay them $30 an hour to do the work, $20 an hour to do the work. We're basically paying AI a lot of money today. The fastest growing software business in the history of mankind. Because now it's doing useful work and we can pay them to do it. Now, that's one view of AI, which is what it can do. But one other view of AI that's really important to help reason through what Constantine saying.

**4:00** · So, for example, the reason why some companies some people are able to build great businesses and could maneuver themselves into the center of very large industries is because when they see this capability, this is very interesting.

**4:11** · One interesting thought is if we're able to do this, what is the implication to the downstream industries?

**4:16** · That's an interesting conversation we should have, okay? So, now that AI can do this, what happens to all the industries like health care and financial services and life sciences and manufacturing, logistics, transportation, on and on and on.

**4:26** · E-tail, advertising, future entertainment, the the list the list of the list of conversations you can have about now that AI can do this, what can it do as a result subsequently? That's an interesting conversation, but you should go upstream, meaning industrially, what does that mean? And so, the first thing you realize is this.

**4:40** · Go back to first principles. I had told you just now that AI is software and it's being produced by computer. Now, what happened to the computer that is made it possible to do this? Well, the big idea is about if you think about the computers we know it today really emerged about 64 years ago. IBM System 360 was the biggest announcement of computing and 64 years ago IBM was the most valuable company in the world, okay? And they created the modern understanding of computers. Everything that we can describe about computer was really described in 1964. For 60 for 40 years largely has remained the same.

**5:08** · And what happened was what happened was that that form of computing is called pre-recording. You write down your story, you save it to a file. You write a program by hand, you save it to a file. You take a picture, you save it to a file, you record music, you save it to a file, you make a video right now, we're in streaming right now, but somebody's going to record it, you're going to save it to a file. And when you want to use it later, you retrieve it from the disk drive. Does that make sense? And the retrieval process is done intelligently.

**5:34** · So, that's why everybody's retrieval of a new story is a little bit different.

**5:37** · It's called a recommender system. But basically, computers as we know it today is a retriever retrieval-based system, which is the reason why these buildings are called data centers. They store data. Notice they don't call them computer centers because not doing much computing. They just store data that you retrieve based on what you touch on your phone. Well, what happened now? If you look at what I just described, in order for this AI to work as I described it, every time I say something to it, I have to give it new information. We call it context. I give it a new prompt. That's called a query.

**6:05** · Between the context and the query, it will understand it first, reason about it, and it will produce an output based on that context and that query, based on the circumstance. Does that make sense so far? Give me one nod, okay? And so, if that is the case, every time you use the AI, the content is produced originally every single time.

**6:24** · Everything I'm saying to you right now is being produced in real time. And it's because my explanation is based on the fact that I realize all of you come from 60 different countries, 128 different families. You all have many different backgrounds. Some of you probably came from the computer industry. Most of you probably did not. And so, I'm explaining the information to you in a way that is sufficiently deep, but ultimately my goal is this, so that you know how to make your next investment. That's what I'm leading to.

**6:48** · And so, I'm going to give you enough sufficient information that you can reason about it for yourself so that when you see something in the next time you go, that's worth investing in.

**6:54** · That's going to be a big industry.

**6:56** · That's a hundred billion dollars right now, and it looks really big, but that's nothing compared to how big it's going to be. I'm going to give you the intuition to solve that problem, okay?

**7:03** · And so, so here we are. Went from a computer industry that was largely based on retrieval for 60 years, and all of a sudden one day it's completely generated in real time. We call it intelligence.

**7:12** · This This is what I'm doing right now for you. I'm demonstrating intelligence.

**7:15** · Contextual awareness. He gave me a prompt, and here comes my answer. Does that make sense? Thanks.

**7:20** · \[laughter\] Extremely artificial intelligence, okay?

**7:25** · And so, and so here I So, here here What's going on now? I just gave you one word earlier. It's called generative AI. The The computer of today has been completely reinvented. It's now generative. And every single Every single letter you see, every single word you see in your in the future, every video, every image, every ad, every TV commercial, every single time you read a story, a new story, every one of them will be different. What Constantine sees, what I see, what you see, will be completely different because it'll be generated for you.

**7:51** · Because your your interest, your context, who you are, for what reason you asked, how you asked, is completely different. Does it make sense? And so, therefore, therefore, every single pixel that you see, every single sound that you hear in the future, every video you see in the future, will be originally generated, not retrieved. Which means, in the future, we need a lot more generators. And these generators is what we build.

**8:13** · That's what we build for a living. These are large computers and they're generating intelligence. Now, the next question is this, well, how big could it be? How big can it be? And so, it turns out, it turns out, the amount of information, the amount of generation of intelligence is we do it for about a billion people in the world today. Now that I told you that AI has become agentic, meaning that it can actually do work by itself. Well, if it can do work by itself, then one agent can communicate with another agent and say, I have some work to do. Let's team up together. Let's do some work. And now you have all these different agents and they're all working together to solve problems inside your company, say.

**8:43** · So, inside our company, Constantine knows that we we're huge users of agentic AI.

**8:49** · We have hundreds of thousands of agents probably running around right now that are doing work and they're talking to each other and they're solving problems. All guarded, all sandboxed, all guarded and sandboxed, but they're all working with each other. Which means, in the future, it is very likely that the internet that we use today for a billion people will likely mostly be several billion, call it a hundred billion agents working around the clock and they're using the internet and talking to each other. And what are they saying?

**9:13** · So, for example, there'll be uh companies working with companies, uh employees agents working with other employees agents, uh there'll be self-driving cars, which are agentic, there'll be robots, which are agentic, all the manufacturing systems, every building will be agentic, there'll be agents all over the place and they'll be using the internet. And all of those commands that they generate to each other will be generated. All of the thoughts that they have to understand, all generated. Does it make And so the basically the world is going to be this layer of computing that's going to cocoon the earth and it's going to be generating intelligence all the time.

**9:44** · Now, I just said something that sounds ridiculous except in fact it's already happened twice. So 300 years ago a company in Germany called Siemens produced a machine and this machine is really interesting machine. You go up to this machine you light it on fire and then this incredible invisible force comes out the other end.

**10:02** · Nobody understood what it was. We understand it now as electricity. How many power generators are there in the world? We call it a grid. Power generation cocoons the planet. We call it the grid. And then of course 20 somewhat years ago, earlier than that, 35 years ago, this networking scheme networking matrix fabric was created here in the United States. Eventually became the internet. And where is it? It cocoons the world. And so now you have energy, communications, intelligence and it will cocoon the world. And we'll use it for, you know, it'll just be a commodity and we'll use it all over the place. And so what Nvidia does for a living is this new machine.

**10:31** · The machine that was invented 300 300 years ago is called the dynamo. That dynamo, anything that moves comes in, could be, you know, waterfalls, it could be wind, fire, steam. Transfer it from motion atoms, right, to electrons. Atoms to electrons. We then take the electrons into our machine called Nvidia. Electrons now comes into our machine, comes in this factory and what comes out are numbers. These numbers, depending on how you combine them, turns into language, math.

**11:00** · It can also turn into a new language we've learned, proteins. We learned the the language of human biology. We learned the language of the physical world, physics, climate, weather. We learned the language of the 3D world, robotics, self-driving cars. We learned the language of all kinds of different forms of intelligence.

**11:16** · But the point being now these two machines, 300 years apart, atoms in, electrons out, electrons in, numbers out. And those numbers could be rejiggered, reformulated into all kinds of different intelligence. That's what we built, that's what we do for a living and that's why I call it a factory because it's producing, we call them tokens but they're just numbers, tokens, and these tokens are intelligence. That's it. That's what we do. It's not that hard.

**11:38** · Brilliant.

**11:41** · \[applause\] Now you know what AI's for, and now you know what AI's how AI's built, and how how \[clears throat\] big it's going to be.

**11:48** · We're in the middle of this revolution.

**11:49** · We're you could say decades in, you could say years in, certainly now in the the mainstream of the intelligence revolution. How do we participate? I'm sure everybody here wants to participate in this revolution.

**12:00** · Yeah, excellent question.

**12:00** · Let's start with big enterprises, and then let's get to individuals as well.

**12:04** · How do people join this movement?

**12:06** · And so now I gave you two mental models.

**12:07** · I'm going to give you one more mental model. So one mental model, they're they're really, you know, we could talk about the story and hopefully we cover all four phases. I just talked about what AI can do, I talked about how AI is made, and these things are in these factories. These factories are, you know, each gigawatt is about $50 billion. So if you've ever seen it, it's the most expensive factory in the world, but it also that one $50 billion factory also generates 300-400 billion dollars in intelligence. And so the the production value is incredible, okay?

**12:34** · The return on investment is extremely fast. And so these So that's the factory part. The part that I'm going to tell you now, and this is very important when you think about investment, is what does the industrial layout look like for for AI? And the the way to think about the industrial view is think of it as a five-layer cake. Now I told you on the bottom is energy. The bottom is, remember I said the dynamo, okay? Now we have course different different AC generators and things like that, power generation. And so on the lowest layer is energy. This is the single greatest opportunity in several generations for the energy industries to grow. The very first time in probably, I don't know, 100 years since the energy grid in many countries could be invested in.

**13:06** · This is the best opportunity to invest in sustainable energy. If you care about sustainable energy, nuclear, air, you know, or wind, solar, you name it, whatever form, hydrogen, whatever form, as long as it produces energy, it's going to get funded. And so that tells you something about how great of a time this is because we have a trillion dollars. Just think, this one year this year alone, we're going to put a trillion dollars from the market into this entire five-layer cake. I'm about to describe to you. So, the first layer is energy. That's the reason why Siemens is doing so well, that's Mitsubishi is doing fantastically, GE, Vernova, I mean, everybody. The first layer of the cake is energy.

**13:37** · The second layer of the cake is chips and computers and networking and switches and silicon photonics. Does that make sense? It's all the computers. The third layer of the cake, we call it infrastructure.

**13:47** · Land, power, shell, money, data center operations. Every one of them is in scarce supply today. And so, that's the that's the next layer, it's infrastructure layer. And then the layer that everybody sees, that everybody thinks is AI, is the model layer. Does that make sense? That's the next layer, it sits on top of the computers, the the cloud infrastructure. And this is the greatest opportunity in recent human in human history that I know, that's so much market-driven investment is naturally coming into the ecosystem.

**14:10** · It's a great time to build. And so, so that now that's the model layer. The model layer is OpenAI, it's Anthropic. But this is the part that you can't overlook. This is very important. So, you have two companies that you know of, that you hear about. Um however, don't forget AI as I was explaining earlier, has learned a language. It learns the language and the meaning. The mean The language, the meaning of anything that is structural.

**14:33** · And so, if if you if things are predictable and are predictable, then there's structure you can learn from it and you can learn the meaning of it, okay? And so, we learn the meaning of proteins, we learn the meaning We're learning the meaning of genes, not just sequencing it, not not just CRISPR editing it, but what is the meaning of that gene? What is the meaning of a cell? Why does a cell do what a cell does? What happens if two cells come together? And so, this is no different than Imagine I learn the meaning of a cell the way I learn the meaning of a word. And what what is what happens when I took take two words, put them together? These two words activate each other, turn into something else of another meaning, okay?

**15:00** · And so, from a computer's perspective, it doesn't care if it's a cell, a protein, a word, an image, a car. Does that make sense? It's just tokens. And so, we have to figure out as computer scientists, we have to figure out how to represent the world's information in all these different ways so that the computer can understand it.

**15:17** · Understand Understand it, reason about it, come up with a plan, generate an action, the intelligence loop. Proteins the same way, cells the same way, the human anatomy is the same way. It must be predictable. It's predictable because tomorrow morning I'm largely the same.

**15:28** · It must be predictable, okay? And so, uh we're learning all these different My point is, there are two language models that you guys know about, but AI is a giant industry. The industry of everything else physical is about $80 trillion. It is actually, you know, the most important frontier, the one the parts that we're not talking about. And then, on top of that, this model, this technology, then feeds into all the stuff that Constantine gets to see these days, which is all of these startups that are coming up with revolutionary ideas in financial services, in legal, in accounting, in transportation, logistics, isn't that right?

**15:58** · And so, what that layer above this last year, $100 billion of venture capital investment, the single largest year of VC investment in the history of humanity. All of that money is going into that fifth layer, the top layer, which is the the layer that apply applications to enhance human condition.

**16:17** · And so, there are five layers. When you think about AI and you want to invest in this future, and I promise you this future is going to be gigantic because two years ago zero, it's approximately we're about to put $1 trillion in, but that's $1 trillion out of the, you know, we're going to be putting in probably the AI industry, I'm going to guess for a second, probably something along the lines of $20 trillion a year. We're $1 trillion in of a $20 trillion a year ecosystem. Because the production of intelligence, you just got to ask yourself, how important is intelligence?

**16:44** · And who needs it?

**16:45** · And how much of it do you want? And so, those are kind of the basic questions. And all of that intelligence, whether it's for proteins or cars or robots or language or math, science, whatever it is, has to be generated by these machines. And so, this five-layer cake is the industrial version. And I think that's a good way to think about where to invest.
