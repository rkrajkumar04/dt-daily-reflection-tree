# DT Fellowship Assignment: Design Rationale

## Why I Chose These Questions

While designing this tree, I kept thinking about the actual moment when a tired employee would use it. At the end of the day, most people do not want to fill out something that feels like a personality test or a formal survey. So I wanted the flow to feel more like a short, structured conversation.

I started with a very simple opening question, asking the user to describe the day in one word. I chose that because it is easy to answer and it immediately gives emotional context to the rest of the reflection. From there, I designed the tree so that each axis goes one step deeper.

In Axis 1, I wanted the questions to surface agency without sounding like blame. The point is not to ask, "Was everything your fault?" but rather, "Where did you still have a choice?" That is why the follow-up questions focus on preparation, response, adaptation, or waiting.

In Axis 2, I wanted to shift the reflection from "What did I get today?" toward "What did I give today?" I tried to make the options realistic and honest. Real employees do feel overlooked, and they do get frustrated when others are not pulling their weight. I included those options because if every answer sounds overly noble, the tree becomes fake.

In Axis 3, I wanted the user to widen their frame of attention. I used options like self, team, colleague, and customer because they naturally represent a widening radius of concern. My goal here was not to dismiss personal stress, but to show that meaning often becomes clearer when the user steps slightly outside their own immediate frustration.

## How I Designed The Branching

I used a combination of direct branching and signal-based branching.

Direct branching helps the tree feel responsive. For example, if the user starts the session by describing the day as tough or draining, the next question should not sound the same as it would for someone who said productive or mixed. That first branch makes the conversation feel more natural.

At the same time, I did not want every single option to create a completely separate sub-tree, because that would make the structure too large and harder to maintain. So I used signals to accumulate leanings across each axis. For example, on Axis 1, answers can add to either internal or external locus. Then a later decision node checks which side is dominant and chooses the reflection accordingly.

This approach helped me make the system deterministic without making it feel mechanical. It is still fully traceable as a tree, but the reflections are based on a pattern across multiple answers rather than one isolated response.

The main trade-off I made was keeping the tree medium-sized instead of trying to make every path highly granular. If I had more time, I could build more nuanced mid-spectrum branches. But for this assignment, I felt it was better to build a tree that was clear, coherent, and auditable rather than one that was very large but repetitive.

## Psychological Sources That Informed My Design

I used the three psychological axes given in the prompt as the main foundation.

For Axis 1, I used the idea of locus of control from Julian Rotter, along with the growth mindset framing from Carol Dweck. What mattered to me here was the distinction between total control and meaningful agency. A person may not control the whole situation, but they may still control preparation, escalation, interpretation, or response.

For Axis 2, I used the contrast between psychological entitlement and contribution-oriented behavior. The idea of organizational citizenship behavior was especially useful because it gave me a concrete way to think about everyday contribution: helping someone, teaching, unblocking work, or doing something useful beyond strict role boundaries.

For Axis 3, I used the ideas of self-transcendence and perspective-taking. I found this axis especially interesting because it is not really about suppressing the self. It is about widening the frame so that the person can see team, colleague, or customer impact alongside their own experience.

Overall, I tried to translate these theories into practical fixed-choice questions that a real employee might actually answer honestly at 7 p.m.

## What I Would Improve With More Time

If I had more time, I would improve the project in four main ways.

First, I would add more mixed-path reflections. Right now, the tree captures the major leanings well, but some people will genuinely show both agency and frustration, or both contribution and entitlement, in the same day. I would like to support those middle states more explicitly.

Second, I would expand the summary layer. At the moment, the summary is deterministic and useful, but it could become more tailored by combining multiple axis patterns into different summary templates.

Third, I would build a lightweight web interface. The CLI works well for demonstrating the logic, but a simple UI with progress indication and cleaner transitions would make the reflection experience more natural.

Finally, I would test the tree with real users. The strongest next improvement would come from observing where people hesitate, where two answer options feel too similar, or where a reflection does not land as intended.
