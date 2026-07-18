# Design Skills

*Claude skills for designers: digital design mentors and a positioning coach, by [Tim van den Bosch](https://www.linkedin.com/in/timvdbosch) (Sitelane).*

Een set Claude-skills (Nederlandstalig) die designwerk beoordelen en designers helpen zichzelf te
positioneren. De persona-skills spreken in de stem van de meesters zelf, gevoed met hun eigen
woorden — geen samenvattingen uit het geheugen van een model.

## De skills

| Skill | Wat het doet |
|---|---|
| **stefan-sagmeister-design** | Digital Stefan Sagmeister: beoordeelt werk op schoonheid, emotionele lading en lef. Gevoed met 184 Q&A's van sagmeister.com en zes talk-transcripts (zie installatie). |
| **massimo-vignelli-design** | Digital Massimo Vignelli: discipline, typografie, tijdloosheid, intellectual elegance. |
| **dieter-rams-design** | Digital Dieter Rams: weniger aber besser — verdient elk element zijn bestaan? |
| **designer-positioning** | Positioneringscoach op basis van de talk "Stop applying, start strategizing": portfolio's, LinkedIn-profielen en outreach herschrijven van "begging student" naar "strategic partner". |
| **team-creative-review** | Orchestrator: laat 3-4 meesters parallel hetzelfde werk beoordelen en synthetiseert, met de onderlinge spanningen expliciet (Vignelli wil terughoudendheid waar Sagmeister lef wil — die botsing is de waarde). |

## Installatie

Kopieer (of symlink) de skill-mappen naar `~/.claude/skills/`:

```bash
git clone https://github.com/mondayrunner/design-skills.git
cd design-skills
for d in stefan-sagmeister-design massimo-vignelli-design dieter-rams-design designer-positioning team-creative-review; do
  ln -s "$(pwd)/$d" ~/.claude/skills/$d
done
```

### Sagmeister-references genereren (eenmalig)

De Sagmeister-skill leunt op zijn eigen woorden: de Q&A's van
[sagmeister.com/answers](https://sagmeister.com/answers/) en de transcripts van zes publieke talks.
Die content herpubliceren we hier niet (het is zijn werk, niet het onze) — je genereert hem lokaal:

```bash
cd stefan-sagmeister-design/scripts
./fetch_references.sh   # vereist: curl, python3, yt-dlp
```

Dit vult `references/answers-faq.md` en `references/talks/` in een paar minuten.

## Opmerkingen

- De skills zijn geschreven in het Nederlands maar antwoorden in de taal van de gebruiker; citaten
  van de meesters blijven in het Engels.
- `team-creative-review` verwijst optioneel ook naar persona-skills die niet in dit repo zitten
  (David Ogilvy, Rory Sutherland, Alex Napier Holland). Zonder die skills draait het panel gewoon
  met de beschikbare reviewers.
- De persona's zijn eerbetonen, geen officiële producten van de genoemde ontwerpers. Verzonnen
  quotes zijn in de skills expliciet verboden: staat iets niet in de bronnen, dan zegt de persona
  het in eigen woorden zonder het als citaat te presenteren.

## Licentie

MIT voor de skill-teksten en scripts in dit repo. De content die de scripts ophalen
(sagmeister.com, YouTube) blijft eigendom van de respectievelijke makers.
