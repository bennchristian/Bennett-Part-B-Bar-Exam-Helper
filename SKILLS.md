# Skills and agents for Part B Bar Exam Helper

One winner per job. When several installed skills could plausibly handle a task,
this table decides — and names the ones not to pick, since those are what get
chosen by mistake.

BMAD (v6.12.4, `bmm` module) is installed in `.claude/skills/` for the planning documents.
Most work is study content, though, so most jobs have no skill: the session does them
directly. BMAD's build, story and sprint skills are for software and are not used here.

## Routing

| Job | Winner | Not these |
|---|---|---|
| Product requirements (`PRD.md`) | `bmad-prd` | `bmad-product-brief`, `bmad-prfaq`, `spec`, `bmad-spec` |
| System architecture (`ARCHITECTURE.md`) | `bmad-architecture` | `design-consultation`, `bmad-spec` |
| Visual system (`DESIGN.md`) | `bmad-ux` | `design-and-templates`, `design-html`, `design-consultation` |
| Repo agent instructions (marker block in `AGENTS.md`) | `bmad-project-context` — run last | `init`, `document-generate` |
| Not sure which BMAD skill | `bmad-help` | — |
| Read a course PDF | `anthropic-skills:pdf` (or `pdftotext -layout` for plain text) | `scrape`, `browse` |
| Read a DOCX (dumps, practice questions) | `anthropic-skills:docx` | `document-generate` |
| Read a progress spreadsheet | `anthropic-skills:xlsx` | — |
| Read or update tracker progress | `ArtifactData` tool on the tracker URL (see `SCHEMA.md`) | republishing the artifact |
| Change the tracker page itself | `artifact-design` + `artifact-capabilities`, then `Artifact` publish to the same URL | `design-html`, `design-shotgun`, `canva` |
| Diagram a procedure (e.g. civil timeline) | `artifact-diagramming` | `diagram`, `infographic-and-data-viz`, `figma:*` |
| Build a paper's Reference Pack PDF | `python3 tools/build_pack.py <paper-id>` (ARCHITECTURE AD-6) | `make-pdf`, `anthropic-skills:pdf`, `anthropic-skills:docx`, `document-generate` |
| Write study outlines, set and mark drills | none — do it directly per `RULES.md` | `educational-content-and-how-to`, `carousel-writer` |
| Recurring daily check-in | `schedule` (only if Bennett asks) | `loop` |
| Scaffold planning docs | `scaffold-project` | `init` |

## Delegating to a subagent

Suggest a subagent, do not auto-delegate. It earns its cost when the work is
broad fan-out search across many files — e.g. pulling every past-paper question on one
topic from 2021–2023 PYPs — or independent tasks that can run in parallel. For a single
known file, reading directly is faster than briefing an agent.

## Not in scope here

Social-media suite (`brand-profile`, `caption-writer`, `hook-writer`, `linkedin-*`, `li-*`,
`reels-script`, …), gstack dev suite (`ship`, `qa`, `review`, `benchmark`, …), iOS
(`ios-*`), Figma (`figma:*`), `claude-for-nonprofits:*`, and BMAD's software-delivery
skills (`bmad-build`, `bmad-build-auto`, `bmad-agent-dev`, `bmad-create-epics-and-stories`,
`bmad-sprint-planning`, `bmad-qa-generate-e2e-tests`, `bmad-code-review`, `bmad-review`).

These are installed but are not competing for any job in this project. Listing
them here keeps them out of the routing table above.

## Maintaining this file

Re-check it when the installed skill set changes. A row naming a skill that is
no longer installed sends the agent after something that is not there, which is
worse than having no table. If a winner loses in practice, change the row rather
than routing around it.
