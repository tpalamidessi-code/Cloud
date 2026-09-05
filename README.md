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

Every brief is committed to `briefs/YYYY-MM-DD.md`. The archive doubles as the
agent's memory — it is how each run knows what was already reported and can
distinguish a genuinely new development from yesterday's story.

## Changing it

- **Coverage, tone, format** — edit `.claude/skills/peptide-brief/SKILL.md`.
  The next scheduled run picks up the change automatically.
- **Schedule or delivery** — ask Claude to update the Routine.

## Note

Informational only, not legal advice.

## Setup status

Complete. The Routine **"Daily Peptide & GLP-1 Brief (8:00 AM ET)"** is enabled,
scheduled, and has the Gmail connector attached, so scheduled runs can send the
email themselves.

If email delivery ever stops, check that connector first — open the routine at
`claude.ai/code/routines` and confirm Gmail is still enabled on it. The brief spec
degrades gracefully if it is missing: the run still commits the brief to `briefs/`
and sends a push notification, and says explicitly that email was skipped.

## Daylight saving

The schedule is stored in UTC as `3 12 * * *`, which is 8:03 AM Eastern **while
EDT is in effect**. When the US falls back to EST in early November, that becomes
7:03 AM ET. Change the Routine's cron to `3 13 * * *` then to hold 8 AM, and back
to `3 12 * * *` in March.
