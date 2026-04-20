# DT Fellowship Assignment: Design Rationale

## Why These Questions

I designed the tree as one continuous evening conversation rather than three separate quizzes. The opening question asks for a simple emotional label because that is cognitively easy at the end of a workday and creates a natural branch into Axis 1. From there, the questions gradually move from surface description to deeper interpretation:

- Axis 1 asks how the employee interpreted what happened and where they still had some choice.
- Axis 2 shifts from interpretation to contribution by asking what they gave in one concrete interaction.
- Axis 3 widens the frame from personal experience to team, colleague, or customer impact.

Each question uses fixed options that are psychologically meaningful but still realistic. I avoided obviously “good” and “bad” answers because the assignment emphasizes reflection without moralizing. For example, “I felt overlooked” and “I was frustrated that others were not doing their part” are plausible end-of-day thoughts, not strawman options.

## Branching Logic And Trade-Offs

The tree uses three kinds of branching:

- Early answer-based routing to keep the conversation context-sensitive.
- Signal accumulation across each axis to detect the dominant leaning.
- Reflection selection based on the dominant pole on that axis.

This hybrid design let me keep the tree deterministic while still making it feel conversational. If I had used only direct answer-to-answer routing, the experience would become brittle and too literal. If I had used only score tallies, the experience would feel like a hidden quiz. Combining both created a better balance: the user gets relevant follow-up questions, but the reflections still synthesize across multiple answers.

One trade-off is that I kept the tree moderately sized rather than exhaustively branching every option into a unique path. That was intentional. The assignment values structure and thoughtfulness, and a medium-sized tree is easier to audit, extend, and implement correctly in a short timeline than a very large one with redundant sub-branches.

## Psychological Sources

The tree was informed by the three source frames in the prompt:

- Julian Rotter on locus of control, especially the difference between agency and externalization.
- Carol Dweck on growth mindset, particularly the belief that response and strategy matter even when outcomes are imperfect.
- Campbell et al. on psychological entitlement and Organ on organizational citizenship behavior, which informed the contribution versus expectation framing.
- Maslow’s later work on self-transcendence and Batson’s work on perspective-taking, which informed the widening-radius questions.

The practical design interpretation was:

- Axis 1 should surface agency without implying total control.
- Axis 2 should surface contribution without shaming unmet needs for fairness or recognition.
- Axis 3 should expand perspective without denying the employee’s own stress.

## What I Would Improve With More Time

With more time, I would improve the project in four ways:

- Add more mid-spectrum branches for genuinely mixed cases, especially users who alternate between agency and frustration in the same day.
- Create multiple summary templates keyed to dominant-pattern combinations so the ending feels even more tailored while staying deterministic.
- Build a lightweight web UI with progress indication and session history.
- Run usability tests with real users and revise any options that feel too close together or too easy to game.
