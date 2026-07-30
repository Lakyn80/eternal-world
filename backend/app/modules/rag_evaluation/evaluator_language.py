from __future__ import annotations

# Extra lack-of-evidence markers beyond the base list in evaluator.py
RUSSIAN_LACK_OF_EVIDENCE_MARKERS = (
    "не помню",
    "не помню об этом",
    "к сожалению, не помню",
    "к сожалению, я этого не помню",
    "я этого не помню",
    "мне это не вспоминается",
    "в сохранённых воспоминаниях нет",
    "в сохраненных воспоминаниях нет",
    "в сохранённых воспоминаниях у меня нет",
    "в сохраненных воспоминаниях у меня нет",
    "в моих сохранённых воспоминаниях нет",
    "в моих сохраненных воспоминаниях нет",
    "этой информации нет",
    "нет информации",
    "не могу подтвердить",
    "не могу этого подтвердить",
    "такого опыта нет",
    "этого опыта у меня нет",
    "не располагаю",
    "об этом нет",
)

RUSSIAN_LACK_DENIAL_CONTEXT_MARKERS = (
    *RUSSIAN_LACK_OF_EVIDENCE_MARKERS,
    "ничего нет",
    "не подтверждаю",
    "не могу рассказать",
    "подробностей нет",
)

# Latin marker / alias -> Cyrillic answer forms (substring match in normalized answer)
CYRILLIC_MARKER_ALIASES: dict[str, tuple[str, ...]] = {
    "brno": ("брно", "брн"),
    "brn": ("брно", "брн"),
    "václav": ("вацлав", "вацлава"),
    "vaclav": ("вацлав", "вацлава"),
    "pavel": ("павел", "павла", "павл"),
    "pavla": ("павел", "павла", "павл"),
    "balaton": ("балатон",),
    "ludm": ("людм", "людмила"),
    "ludmila": ("людм", "людмила"),
    "mikulov": ("микулов",),
    "popice": ("попиц",),
    "vídeň": ("вен", "віден"),
    "viden": ("вен", "віден"),
    "vienna": ("вен", "віден", "вена"),
    "literatur": ("литерат", "литератур"),
    "литерат": ("литерат", "литератур", "literatur"),
    "horákov": ("гораков", "хораков"),
    "novotn": ("новотн",),
    "tereza": ("терез",),
    "teréza": ("терез",),
    "klára": ("клар",),
    "klara": ("клар",),
    "líšn": ("лишень", "лишн"),
    "lisen": ("лишень", "лишн"),
    "řečkovic": ("ржечковиц",),
    "reckovice": ("ржечковиц",),
    "book": ("книг",),
    "knih": ("книг",),
    "несем": ("nesem",),
    "новин": ("noviny", "novin"),
}


def expand_marker_aliases(normalized_marker: str) -> tuple[str, ...]:
    aliases = CYRILLIC_MARKER_ALIASES.get(normalized_marker, ())
    return (normalized_marker, *aliases)
