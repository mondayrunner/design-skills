# Design Skills

*Claude skills for designers, by [Tim van den Bosch](https://www.linkedin.com/in/timvdbosch) (Sitelane).*

Digitale designmentors als Claude-skills (Nederlandstalig). De persona's spreken in de stem van de
meesters zelf, gevoed met hun eigen woorden: FAQ's, talks en interviews. Geen samenvattingen uit het
geheugen van een model.

## De skills

| Skill | Wat het doet |
|---|---|
| **stefan-sagmeister-design** | Digital Stefan Sagmeister: beoordeelt werk op schoonheid, emotionele lading en lef. Gevoed met 184 Q&A's van sagmeister.com en zes uur aan talks. |
| **massimo-vignelli-design** | Digital Massimo Vignelli: discipline, typografie, tijdloosheid, intellectual elegance. |
| **dieter-rams-design** | Digital Dieter Rams: weniger aber besser — verdient elk element zijn bestaan? |
| **designer-positioning** | Positioneringscoach: portfolio's, LinkedIn-profielen en outreach herschrijven van "begging student" naar "strategic partner". |
| **team-creative-review** | Orchestrator: laat meerdere meesters parallel hetzelfde werk beoordelen, met de onderlinge spanningen expliciet. Vignelli wil terughoudendheid waar Sagmeister lef wil; die botsing is de waarde. |

## Installatie

```bash
git clone https://github.com/mondayrunner/design-skills.git
cd design-skills
for d in stefan-sagmeister-design massimo-vignelli-design dieter-rams-design designer-positioning team-creative-review; do
  ln -s "$(pwd)/$d" ~/.claude/skills/$d
done
```

De skills antwoorden in de taal van de gebruiker; citaten van de meesters blijven in het Engels.
Het review-panel schaalt mee met je eigen persona-skills: extra reviewers voeg je toe via het
prompt-sjabloon in `team-creative-review/SKILL.md`.

## Sagmeister-references verversen

De Q&A's en transcripts van de Sagmeister-skill staan meegeleverd in `references/`. Verversen kan met:

```bash
cd stefan-sagmeister-design/scripts && ./fetch_references.sh   # vereist: curl, python3, yt-dlp
```

## Disclaimer & licentie

De persona's zijn eerbetonen, geen officiële producten van de genoemde ontwerpers. Verzonnen quotes
zijn in de skills expliciet verboden. MIT-licentie voor de skill-teksten en scripts; de meegeleverde
bron-content (sagmeister.com-FAQ, talk-transcripts) blijft eigendom van de respectievelijke makers
en wordt op verzoek verwijderd.
