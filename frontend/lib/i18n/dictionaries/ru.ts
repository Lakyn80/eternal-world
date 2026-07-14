/**
 * Russian dictionary (Task 64.5.1). Seeded verbatim from the existing
 * Russian-only UI strings already shipped in
 * ../../components/family-memory-review-page.tsx and
 * ../../components/fa-chat-demo-page.tsx, so the Russian interface's
 * wording is preserved exactly - not re-authored.
 */
const ru = {
  nav: {
    home: "Демо Eternal World",
    chatWithAvatar: "Чат с аватаром",
    familyMemoryReview: "Проверка семейных воспоминаний",
    goToChat: "Перейти в чат",
    goToReview: "Проверка семейных воспоминаний",
    backToChat: "Вернуться в чат",
    czech: "Чешский",
    russian: "Русский",
    switchLanguage: "Переключить язык",
  },
  homePage: {
    eyebrow: "Вечный мир",
  },
  demoWarning:
    "Демо-режим: личность и семейная роль участника имитируются выбором ниже. Не используйте этот интерфейс с реальными приватными семейными данными.",
  demoWarningChat:
    "Демо-режим: идентификация и семейные роли имитируются. Не используйте реальные приватные семейные данные.",
  actorBar: {
    label: "Демо-роль участника",
    technicalDetails: "технические детали",
    ownerLabel: "Владелец аватара (Ева)",
    contributorLabel: "Внучка Анна (участник семьи)",
  },
  eyebrow: "Вечный мир",
  reviewTitle: "Проверка семейных воспоминаний",
  inbox: {
    ariaLabel: "Список эпизодов на проверке",
    filters: {
      all: "Все",
      needs_review: "Требует проверки",
      collecting_details: "Сбор деталей",
      ready_for_owner_review: "Готово к проверке",
      approved: "Подтверждено",
      rejected: "Отклонено",
      disputed: "Спорное",
      pending_index: "Ожидает индексации",
      indexed: "Проиндексировано",
    },
    emptyNoEpisodes: "Пока нет эпизодов, предложенных членами семьи.",
    emptyFiltered: "Нет эпизодов с выбранным статусом.",
    loadError: "Не удалось загрузить список эпизодов.",
    retry: "Повторить попытку",
    contributorFrom: "от",
    contributorUnknown: "участник неизвестен",
    unresolvedQuestions: "вопросов без ответа",
  },
  reviewStatus: {
    needs_review: "Требует проверки",
    approved: "Подтверждено",
    rejected: "Отклонено",
    archived: "В архиве",
  },
  enrichmentStatus: {
    draft: "Черновик",
    collecting_details: "Сбор деталей",
    ready_for_owner_review: "Готово к проверке",
  },
  disputeStatus: {
    none: "Без спора",
    disputed: "Спорное",
    resolved: "Спор разрешён",
  },
  promotionStatus: {
    pending_index: "Ожидает индексации",
    indexed: "Проиндексировано",
    failed: "Ошибка индексации",
    cancelled: "Отменено",
  },
  contributionType: {
    initial_claim: "Первоначальный рассказ",
    clarification_answer: "Ответ на уточнение",
    owner_correction: "Правка владельца",
    owner_confirmation: "Подтверждение владельца",
    reviewer_note: "Заметка проверяющего",
    dispute_statement: "Заявление о споре",
    system_normalization: "Системная нормализация",
  },
  clarificationStatus: {
    pending: "Ожидает ответа",
    answered: "Отвечено",
    skipped: "Пропущено",
    cancelled: "Отменено",
  },
  privacyScope: {
    private_owner: {
      label: "Только владелец",
      description: "Можно подтвердить, но пока нельзя проиндексировать.",
    },
    selected_family: {
      label: "Выбранные родственники",
      description:
        "Можно подтвердить, но индексация недоступна, пока не появится учёт прав доступа по кругу семьи.",
    },
    all_family: {
      label: "Вся семья",
      description: "Может быть проиндексировано после подтверждения.",
    },
    public_legacy: {
      label: "Публичное наследие",
      description: "Может быть проиндексировано после подтверждения.",
    },
  },
  blockedReasons: {
    legacy_workflow_not_supported_in_review_ui: "Это старый формат эпизода без семейной проверки.",
    actor_is_not_owner: "Только владелец аватара может выполнять это действие.",
    candidate_review_already_terminal: "Проверка этого эпизода уже завершена.",
    collecting_details: "Ожидаются ответы на уточняющие вопросы.",
    not_ready_for_review: "Эпизод ещё не готов к проверке владельцем.",
    disputed: "Есть неразрешённое расхождение во мнениях.",
    not_promoted_yet: "Эпизод ещё не подтверждён владельцем.",
    privacy_scope_not_indexable: "При текущей области приватности индексация недоступна.",
    russian_translation_missing: "Русский перевод ещё не готов.",
    russian_translation_failed: "Не удалось выполнить перевод на русский язык.",
    russian_translation_stale: "Русский перевод устарел и не соответствует текущему тексту.",
  },
  actions: {
    confirm: "Подтвердить",
    edit_and_confirm: "Сохранить и подтвердить",
    reject: "Отклонить",
    request_more_details: "Запросить больше деталей",
    mark_disputed: "Отметить как спорное",
    approve_multiple_perspectives: "Подтвердить с разными точками зрения",
    indexMemory: "Индексировать воспоминание",
  },
  detail: {
    ariaLabel: "Карточка эпизода",
    selectPrompt: "Выберите эпизод слева, чтобы увидеть подробности.",
    loadError: "Не удалось загрузить карточку эпизода.",
    contributorNotice:
      "Вы просматриваете эпизод как участник семьи. Подтверждение, отклонение и другие решения доступны только владельцу аватара.",
    availableToAvatar: "Доступно аватару",
    notYetAvailableToAvatar: "Пока не используется аватаром",
    technicalData: "Технические данные",
    contributionHistoryTitle: "История дополнений (только для чтения)",
    contributionHistoryEmpty: "Пока нет записей истории.",
    clarificationsTitle: "Уточняющие вопросы",
    clarificationsEmpty: "Дополнительных вопросов не задавалось.",
    answeredAt: "Отвечено",
    requiredSuffix: "обязательный",
    optionalSuffix: "необязательный",
    disputeTitle: "Разные точки зрения",
    disputeWarning:
      "Это воспоминание содержит разные приписанные точки зрения. Подтверждение сохраняет расхождение, а не выбирает одну версию как достоверную.",
    ownerPerspective: "Точка зрения владельца",
    contributorPerspective: "Точка зрения участника семьи",
    finalTextTitle: "Итоговый текст воспоминания",
    resetOriginalText: "Вернуть исходный текст",
    textEditedNotice:
      "Текст отличается от сохранённого на сервере варианта. Изменение будет сохранено как отдельная правка владельца в истории.",
    privacyTitle: "Область приватности",
    actionsTitle: "Действия владельца",
    reviewNotePlaceholder: "Необязательная заметка к решению...",
    switchToOwnerNotice: "Переключитесь на демо-роль владельца выше, чтобы выполнять действия проверки.",
    rejectionReasonLabel: "Причина отклонения (необязательно)",
    promotionTitle: "Продвижение и индексация",
    promotionCreatedAt: "Создано",
    promotionIndexFailed:
      "Индексация подтверждённого воспоминания не выполнена. Повторная попытка сейчас недоступна в этом интерфейсе.",
    promotionNotYetCreated:
      "Продвижение появится после подтверждения владельцем с областью приватности, доступной для индексации.",
    ownerCorrection: "правка владельца",
    disputedSuffix: "спорно",
  },
  translationPanel: {
    title: "Чешский оригинал / Русская версия",
    sourceLabel: "Оригинал",
    czechSourceHeading: "Чешский оригинал",
    russianVersionHeading: "Русская версия",
    sourceOfCzechOrigin: "Источник: чешский оригинал",
    statusOriginal: "Оригинал",
    statusTranslated: "Переведено",
    statusPending: "Ожидает перевода",
    statusFailed: "Перевод не выполнен",
    statusStale: "Перевод устарел",
    statusHumanReviewed: "Проверено человеком",
    retryTranslation: "Повторить перевод",
    lastTranslatedAt: "Последний перевод",
    cannotIndexNotice: "Эту память нельзя проиндексировать без действующего перевода на русский язык.",
    noTranslationYet: "Перевод пока не запрашивался.",
  },
  errors: {
    translationFailed: "Перевод не выполнен.",
    russianPending: "Русская версия ожидает обновления.",
    statusChanged: "Состояние эпизода изменилось на сервере. Данные обновлены, проверьте текущий статус.",
    serverUnavailable: "Не удалось связаться с сервером. Проверьте подключение.",
    tryAgain: "Попробовать снова",
    genericAction: "Не удалось выполнить действие. Попробуйте ещё раз.",
    promotionStateChanged: "Состояние продвижения изменилось на сервере. Данные обновлены.",
  },
  confirmDialog: {
    titlePrefix: "Подтвердите действие:",
    episodeLabel: "Эпизод:",
    untitled: "без названия",
    privacyLabel: "Область приватности:",
    promotionWillBeCreated: "Будет создано продвижение воспоминания, ожидающее явной индексации.",
    promotionWillNotBeCreated: "Продвижение не будет создано автоматически при текущей области приватности.",
    indexingExplanation: "Индексация сделает воспоминание доступным аватару для использования в ответах.",
    cancel: "Отмена",
    confirm: "Подтвердить",
  },
  resultMessages: {
    approved: "Эпизод подтверждён владельцем.",
    rejected: "Эпизод отклонён.",
    statusUpdated: "Статус эпизода обновлён.",
    alreadyIndexed: "Это воспоминание уже было проиндексировано ранее.",
    indexed: "Аватар теперь может использовать это воспоминание.",
  },
  chat: {
    avatarName: "Ева Новакова",
    avatarMonogram: "ЕН",
    avatarRole: "Тёплый семейный аватар",
    eyebrow: "Аватар Евы Новаковой",
    title: "Тестовый чат с цифровым аватаром",
    lead: "Этот демо-аватар отвечает по-русски, держится тёплого человеческого тона и опирается только на сохранённые воспоминания. Если подтверждения нет, он не придумывает факты и мягко скажет об этом.",
    examples: [
      "Где ты жила в детстве?",
      "Бабушка, мне сегодня тяжело.",
      "Ты помнишь, как пела мне песню перед сном?",
    ],
    brand: "Вечный мир",
    subhead: "Ева рядом, когда нужен голос памяти",
    reviewLink: "Семейные воспоминания на проверке",
    debugLabel: "debug",
    clear: "Очистить",
    emptyTitle: "С чего начать",
    emptyText:
      "Спроси о детстве, поддержке или о возможном семейном воспоминании. Если воспоминание не подтверждено, чат отметит его как эпизод для проверки.",
    you: "Вы",
    lackOfEvidenceHint: "Точного подтверждения в доступных воспоминаниях сейчас нет.",
    newEpisodeCardTitle: "Новый эпизод для проверки",
    loading: "Ева подбирает ответ...",
    usedMemoriesSummary: "Использованные воспоминания",
    noPreview: "Короткий фрагмент недоступен.",
    composerHint: "Для наиболее обоснованного ответа лучше спрашивать Еву в первом лице.",
    composerPlaceholder: "Напишите Еве вопрос или тёплое сообщение...",
    composerAriaLabel: "Сообщение для аватара",
    send: "Отправить",
    genericError: "Не удалось получить ответ. Попробуйте ещё раз.",
  },
};

export default ru;

/** Deliberately NOT `as const`: property values are widened to plain
 * `string`/`string[]` (not literal types), so `cs.ts` (or any future
 * locale) is type-checked for having the same keys with any translated
 * string content - not for matching Russian text verbatim. */
export type Dictionary = typeof ru;
