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
