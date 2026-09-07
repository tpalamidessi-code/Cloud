# Peptide & GLP-1 Daily Intelligence Brief

An automated analyst that sweeps FDA primary sources, court dockets, and the news
each morning and emails a brief on what changed in the peptide / GLP-1 world.

## What it watches

| Beat | Coverage |
|---|---|
| FDA | Approvals, CRLs, warning & untitled letters, cease-and-desist actions, 503A/503B compounding enforcement, the 503A bulks list, drug-shortage status for semaglutide/tirzepatide, recalls, import alerts |
| Litigation | Eli Lilly and Novo Nordisk suits against compounders, med spas, telehealth platforms, and research-use-only peptide sellers; retatrutide enforcement; FTC and state AG actions; class actions |
| Policy | DEA scheduling, state peptide laws, USP monographs, DSHEA/NDI status of peptides, compounding legislation |
| Pipeline | Retatrutide (TRIUMPH), tirzepatide, semaglutide, orforglipron, CagriSema, survodutide, mazdutide; trial readouts and filings |
| Market | Pricing (LillyDirect, NovoCare), supply, telehealth strategy, payer coverage |

News sources: Reuters, AP, CNBC, Fox News/Business, CNN, NBC, ABC, CBS, WSJ,
Bloomberg, plus the trades that break this beat first — STAT, Endpoints,
Fierce Pharma, RAPS Regulatory Focus, Pink Sheet.

## How it runs

A scheduled Routine fires a fresh Claude session every morning at **8:00 AM ET**.
That session loads `.claude/skills/peptide-brief/SKILL.md` and follows it:
reads the last three briefs so it doesn't repeat itself, sweeps all five beats,
writes the brief, commits it to `briefs/`, and emails it to tpalamidessi@gmail.com.

Quiet days produce a short "No material developments" brief rather than filler.

## Archive

Briefs written from an interactive session are committed to `briefs/YYYY-MM-DD.md`.
Scheduled runs do **not** archive here — they have no repo — so the folder is a
partial record, not a complete one. The email history in Gmail is the full archive.

## Changing it

- **Coverage, tone, format** — edit `.claude/skills/peptide-brief/SKILL.md`.
  The next scheduled run picks up the change automatically.
- **Schedule or delivery** — ask Claude to update the Routine.

## Note

Informational only, not legal advice.

## Delivery

The scheduled 8:03 AM ET run emails the brief to tpalamidessi@gmail.com through the
Gmail connector attached to the Routine, and the platform sends a completion
notification. Verified working unattended on 2026-09-06 and 2026-09-07.

Arrival time varies by 15-20 minutes — the scheduler adds jitter, so a brief landing
at 8:20 is normal, not a failure.

The routine prompt is deliberately **self-contained**: it reads no files, needs no
repository, and never explores the filesystem. That is not incidental — see the note
in the skill file. Scheduled runs have no repo checked out, and the old prompt's
reference to one sent the agent searching, which tripped a permission prompt that
nobody was there to approve, hanging the run before it ever delivered.

Keep it that way. Anything the daily brief depends on belongs **in the prompt**, not
in this repo.

## Archive## Archive

Briefs written from an interactive session are committed to `briefs/YYYY-MM-DD.md`.
Scheduled runs do **not** archive here — they have no repo — so the folder is a
partial record, not a complete one. The email history in Gmail is the full archive.

## Changing it

- **Coverage, tone, format** — edit `.claude/skills/peptide-brief/SKILL.md`.
  The next scheduled run picks up the change automatically.
- **Schedule or delivery** — ask Claude to update the Routine.

## Note

Informational only, not legal advice.

## Delivery

The scheduled run does all three: commits the brief to `briefs/`, emails it to
tpalamidessi@gmail.com through the Gmail connector, and sends a push notification.

The Gmail connector must stay attached to the Routine for the email step to work —
it is enabled in the routine settings at `claude.ai/code/routines`. Verified working
from scheduled runs on 2026-09-06.

An earlier version of these docs claimed scheduled runs could not use Gmail. That
was a misdiagnosis: the verification searched for a test-only subject line while the
run had emailed the brief under its normal subject. The bad conclusion was briefly
written into the routine's instructions and cost one morning's delivery.

## Daylight saving

The schedule is stored in UTC as `3 12 * * *`, which is 8:03 AM Eastern **while
EDT is in effect**. When the US falls back to EST in early November, that becomes
7:03 AM ET. Change the Routine's cron to `3 13 * * *` then to hold 8 AM, and back
to `3 12 * * *` in March.
