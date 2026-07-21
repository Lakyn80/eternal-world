import { FormEvent, type ReactNode, useEffect, useMemo, useState } from 'react';
import type { Lang } from '../i18n';
import {
  acceptInvitation,
  answerBiographerQuestion,
  answerCandidateClarification,
  createMemorial,
  fetchMemorial,
  getBiographerEligibility,
  getBiographyStatus,
  getNextBiographerQuestion,
  indexCandidateMemory,
  inviteParticipant,
  listChatMessages,
  listContributions,
  listMembers,
  listMemorials,
  listMemoryCandidates,
  listReviewQueue,
  login,
  MemorialApiError,
  ownerReviewCandidate,
  register,
  reviewContribution,
  sendChatMessage,
  skipBiographerQuestion,
  startBiographyIngestion,
  submitContribution,
  updateBiography
} from '../lib/memorialApi';
import { canInvite, canReview, canSubmitContribution, isActiveMemoryEligible } from '../lib/memorialPermissions';
import { APP_ROOT_PATH, buildMemorialPath, navigate, parseAppRoute, usePathname } from '../lib/router';
import type {
  AuthSession,
  BiographerEligibilityRead,
  BiographerQuestionRead,
  BiographyStatusRead,
  ChatMessageRead,
  ContributionRead,
  InvitationCreateResponse,
  InvitableMemorialRole,
  MembershipRead,
  MemoryCandidateEnrichmentRead,
  MemorialRead,
  OwnerReviewCandidateAction,
  PrivacyScope,
  WorkspaceTab
} from '../types/memorial';

type Copy = {
  kicker: string;
  title: string;
  subtitle: string;
  signInTitle: string;
  signInHelp: string;
  signIn: string;
  createAccount: string;
  fullName: string;
  email: string;
  password: string;
  signedInAs: string;
  signOut: string;
  refresh: string;
  chat: string;
  chatEmpty: string;
  chatPlaceholder: string;
  chatSend: string;
  chatYou: string;
  chatAvatar: string;
  biography: string;
  biographyIntro: string;
  biographyPlaceholder: string;
  biographySave: string;
  biographyStartIngestion: string;
  biographyConfirmNote: string;
  biographyStatusDraft: string;
  biographyStatusReady: string;
  biographyStatusIngesting: string;
  biographyStatusIndexed: string;
  biographyStatusFailed: string;
  biographyStatusStale: string;
  biographyRetry: string;
  biographer: string;
  biographerIntro: string;
  biographerBlockedMissing: string;
  biographerBlockedNotIndexed: string;
  biographerBlockedActive: string;
  biographerDone: string;
  biographerAnswerPlaceholder: string;
  biographerSubmit: string;
  biographerSkip: string;
  candidatesTitle: string;
  candidatesEmpty: string;
  candidateConfirm: string;
  candidateReject: string;
  candidateRequestDetails: string;
  candidateMarkDisputed: string;
  candidateIndexButton: string;
  candidateIndexedLabel: string;
  candidatePendingIndexLabel: string;
  candidateClarificationPending: string;
  candidateClarificationPlaceholder: string;
  candidateClarificationSubmit: string;
  createMemorial: string;
  name: string;
  description: string;
  yourMemorials: string;
  empty: string;
  openWorkspace: string;
  overview: string;
  contributions: string;
  review: string;
  members: string;
  invitations: string;
  role: string;
  submitMemory: string;
  titleLabel: string;
  memoryText: string;
  sourceNote: string;
  privacyScope: string;
  submitForReview: string;
  viewerReadOnly: string;
  noContributions: string;
  notActiveMemory: string;
  activeMemory: string;
  noPending: string;
  approve: string;
  reject: string;
  archive: string;
  inviteParticipant: string;
  inviteHelp: string;
  invitationCreated: string;
  devToken: string;
  tokenNote: string;
  acceptTitle: string;
  acceptHelp: string;
  acceptInvitation: string;
  invitationAccepted: string;
  noToken: string;
  creating: string;
  submitting: string;
  working: string;
  indexingPending: string;
  indexingIndexed: string;
  indexingFailed: string;
  indexingRetired: string;
  backToSite: string;
};

const COPY: Record<Lang, Copy> = {
  en: {
    kicker: 'Family access control',
    title: 'Private memorial workspace',
    subtitle: 'Create a memorial, invite family members, collect contributions and approve only memories that should become active avatar knowledge.',
    signInTitle: 'Sign in to continue',
    signInHelp: 'Use a real account from the backend. The frontend keeps the access token only in memory.',
    signIn: 'Sign in',
    createAccount: 'Create account',
    fullName: 'Full name',
    email: 'Email',
    password: 'Password',
    signedInAs: 'Signed in as',
    signOut: 'Sign out',
    refresh: 'Refresh',
    chat: 'Chat',
    chatEmpty: 'No messages yet. Say hello to start the conversation.',
    chatPlaceholder: 'Write a message...',
    chatSend: 'Send',
    chatYou: 'You',
    chatAvatar: 'Avatar',
    biography: 'Biography',
    biographyIntro: 'Write the memorial\'s initial life story. Nothing becomes avatar memory until you explicitly start indexing.',
    biographyPlaceholder: 'Write the biography here...',
    biographySave: 'Save biography',
    biographyStartIngestion: 'Start indexing',
    biographyConfirmNote: 'After indexing, the avatar may use this biography in its answers.',
    biographyStatusDraft: 'Draft - not indexed yet',
    biographyStatusReady: 'Queued for indexing',
    biographyStatusIngesting: 'Indexing in progress...',
    biographyStatusIndexed: 'Indexed - part of avatar memory',
    biographyStatusFailed: 'Indexing failed',
    biographyStatusStale: 'Edited since last indexing - re-index to update avatar memory',
    biographyRetry: 'Retry indexing',
    biographer: 'Biographer',
    biographerIntro: 'The AI Biographer asks one question at a time to learn more about this person. Answers are never indexed automatically - they go through the same review as any other contribution.',
    biographerBlockedMissing: 'Save the biography first.',
    biographerBlockedNotIndexed: 'Index the biography before starting the Biographer.',
    biographerBlockedActive: 'Please finish answering the current clarification question below before continuing.',
    biographerDone: 'All Biographer topics for this memorial have been covered.',
    biographerAnswerPlaceholder: 'Write your answer...',
    biographerSubmit: 'Submit answer',
    biographerSkip: 'Skip this question',
    candidatesTitle: 'Biographer memories',
    candidatesEmpty: 'No Biographer-sourced memories yet.',
    candidateConfirm: 'Confirm',
    candidateReject: 'Reject',
    candidateRequestDetails: 'Request more details',
    candidateMarkDisputed: 'Mark disputed',
    candidateIndexButton: 'Index memory',
    candidateIndexedLabel: 'Indexed and searchable',
    candidatePendingIndexLabel: 'Approved, not yet indexed',
    candidateClarificationPending: 'The Biographer needs one more detail before this can be reviewed:',
    candidateClarificationPlaceholder: 'Write your answer...',
    candidateClarificationSubmit: 'Submit',
    createMemorial: 'Create memorial',
    name: 'Name',
    description: 'Description',
    yourMemorials: 'Your memorials',
    empty: 'No memorials are available for this account yet.',
    openWorkspace: 'Open workspace',
    overview: 'Overview',
    contributions: 'Contributions',
    review: 'Review',
    members: 'Members',
    invitations: 'Invitations',
    role: 'Role',
    submitMemory: 'Submit a memory',
    titleLabel: 'Title',
    memoryText: 'Memory text',
    sourceNote: 'Source note',
    privacyScope: 'Privacy scope',
    submitForReview: 'Submit for review',
    viewerReadOnly: 'Viewers cannot submit memories.',
    noContributions: 'No contributions are visible for this role.',
    notActiveMemory: 'Not active memory',
    activeMemory: 'Active-memory eligible',
    noPending: 'No pending contributions.',
    approve: 'Approve',
    reject: 'Reject',
    archive: 'Archive',
    inviteParticipant: 'Invite participant',
    inviteHelp: 'Owners can invite trusted reviewers, contributors or viewers.',
    invitationCreated: 'Invitation created.',
    devToken: 'Development invite token',
    tokenNote: 'Shown because the backend returned it for dev/test flow. It is not stored in browser storage.',
    acceptTitle: 'Accept invitation',
    acceptHelp: 'Sign in with the invited account. The token is used once from the URL.',
    acceptInvitation: 'Accept invitation',
    invitationAccepted: 'Invitation accepted.',
    noToken: 'Invitation token is missing.',
    creating: 'Creating',
    submitting: 'Submitting',
    working: 'Working',
    indexingPending: 'Approved, indexing pending',
    indexingIndexed: 'Indexed and searchable',
    indexingFailed: 'Indexing failed',
    indexingRetired: 'No longer active evidence',
    backToSite: 'Back to site'
  },
  cs: {
    kicker: 'Kontrola rodinného přístupu',
    title: 'Soukromý memorial workspace',
    subtitle: 'Vytvořte memorial, pozvěte rodinu, sbírejte vzpomínky a schvalte jen to, co se má stát aktivní znalostí avatara.',
    signInTitle: 'Přihlaste se',
    signInHelp: 'Použijte skutečný účet z backendu. Frontend drží access token pouze v paměti.',
    signIn: 'Přihlásit',
    createAccount: 'Vytvořit účet',
    fullName: 'Celé jméno',
    email: 'E-mail',
    password: 'Heslo',
    signedInAs: 'Přihlášen jako',
    signOut: 'Odhlásit',
    refresh: 'Obnovit',
    chat: 'Chat',
    chatEmpty: 'Zatím žádné zprávy. Napište pozdrav a začněte konverzaci.',
    chatPlaceholder: 'Napište zprávu...',
    chatSend: 'Odeslat',
    chatYou: 'Vy',
    chatAvatar: 'Avatar',
    biography: 'Životopis',
    biographyIntro: 'Napište počáteční životní příběh memorialu. Nic se nestane pamětí avatara, dokud výslovně nespustíte indexaci.',
    biographyPlaceholder: 'Sem napište životopis...',
    biographySave: 'Uložit životopis',
    biographyStartIngestion: 'Spustit indexaci',
    biographyConfirmNote: 'Po zaindexování může avatar tento životopis použít ve svých odpovědích.',
    biographyStatusDraft: 'Koncept - zatím neindexováno',
    biographyStatusReady: 'Čeká na indexaci',
    biographyStatusIngesting: 'Probíhá indexace...',
    biographyStatusIndexed: 'Zaindexováno - součást paměti avatara',
    biographyStatusFailed: 'Indexace selhala',
    biographyStatusStale: 'Upraveno od poslední indexace - spusťte indexaci znovu, aby se paměť avatara aktualizovala',
    biographyRetry: 'Zkusit indexaci znovu',
    biographer: 'AI biograf',
    biographerIntro: 'AI biograf klade vždy jednu otázku, aby se dozvěděl víc o tomto člověku. Odpovědi se nikdy neindexují automaticky - projdou stejnou kontrolou jako jakýkoli jiný příspěvek.',
    biographerBlockedMissing: 'Nejprve uložte životopis.',
    biographerBlockedNotIndexed: 'Před spuštěním biografa nejprve zaindexujte životopis.',
    biographerBlockedActive: 'Nejprve prosím odpovězte na aktuální upřesňující otázku níže.',
    biographerDone: 'Všechna témata AI biografa pro tento memorial už byla probrána.',
    biographerAnswerPlaceholder: 'Napište svou odpověď...',
    biographerSubmit: 'Odeslat odpověď',
    biographerSkip: 'Přeskočit otázku',
    candidatesTitle: 'Vzpomínky od biografa',
    candidatesEmpty: 'Zatím žádné vzpomínky od AI biografa.',
    candidateConfirm: 'Potvrdit',
    candidateReject: 'Odmítnout',
    candidateRequestDetails: 'Vyžádat více podrobností',
    candidateMarkDisputed: 'Označit jako sporné',
    candidateIndexButton: 'Zaindexovat vzpomínku',
    candidateIndexedLabel: 'Zaindexováno a vyhledatelné',
    candidatePendingIndexLabel: 'Schváleno, zatím nezaindexováno',
    candidateClarificationPending: 'AI biograf potřebuje ještě jeden detail, než se to dá zkontrolovat:',
    candidateClarificationPlaceholder: 'Napište svou odpověď...',
    candidateClarificationSubmit: 'Odeslat',
    createMemorial: 'Vytvořit memorial',
    name: 'Jméno',
    description: 'Popis',
    yourMemorials: 'Vaše memorialy',
    empty: 'Tento účet zatím nemá žádný memorial.',
    openWorkspace: 'Otevřít workspace',
    overview: 'Přehled',
    contributions: 'Vzpomínky',
    review: 'Kontrola',
    members: 'Členové',
    invitations: 'Pozvánky',
    role: 'Role',
    submitMemory: 'Přidat vzpomínku',
    titleLabel: 'Název',
    memoryText: 'Text vzpomínky',
    sourceNote: 'Poznámka ke zdroji',
    privacyScope: 'Soukromí',
    submitForReview: 'Odeslat ke kontrole',
    viewerReadOnly: 'Viewer nemůže přidávat vzpomínky.',
    noContributions: 'Pro tuto roli nejsou viditelné žádné vzpomínky.',
    notActiveMemory: 'Není aktivní paměť',
    activeMemory: 'Vhodné pro aktivní paměť',
    noPending: 'Nic nečeká na kontrolu.',
    approve: 'Schválit',
    reject: 'Odmítnout',
    archive: 'Archivovat',
    inviteParticipant: 'Pozvat účastníka',
    inviteHelp: 'Vlastník může pozvat trusted reviewera, contributora nebo viewera.',
    invitationCreated: 'Pozvánka vytvořena.',
    devToken: 'Vývojový invite token',
    tokenNote: 'Zobrazeno, protože backend token vrací pro dev/test flow. Neukládá se do browser storage.',
    acceptTitle: 'Přijmout pozvánku',
    acceptHelp: 'Přihlaste se účtem pozvaného člověka. Token se použije jednou z URL.',
    acceptInvitation: 'Přijmout pozvánku',
    invitationAccepted: 'Pozvánka přijata.',
    noToken: 'Chybí token pozvánky.',
    creating: 'Vytvářím',
    submitting: 'Odesílám',
    working: 'Pracuji',
    indexingPending: 'Schváleno, čeká na indexaci',
    indexingIndexed: 'Indexováno a vyhledatelné',
    indexingFailed: 'Indexace selhala',
    indexingRetired: 'Již není aktivní znalost',
    backToSite: 'Zpět na web'
  },
  ru: {
    kicker: 'Семейный контроль доступа',
    title: 'Приватное пространство мемориала',
    subtitle: 'Создайте мемориал, пригласите семью, собирайте воспоминания и одобряйте только то, что должно стать активной памятью аватара.',
    signInTitle: 'Войдите',
    signInHelp: 'Используйте реальный аккаунт backend. Frontend держит access token только в памяти.',
    signIn: 'Войти',
    createAccount: 'Создать аккаунт',
    fullName: 'Полное имя',
    email: 'E-mail',
    password: 'Пароль',
    signedInAs: 'Вошли как',
    signOut: 'Выйти',
    refresh: 'Обновить',
    chat: 'Чат',
    chatEmpty: 'Пока нет сообщений. Напишите привет, чтобы начать разговор.',
    chatPlaceholder: 'Напишите сообщение...',
    chatSend: 'Отправить',
    chatYou: 'Вы',
    chatAvatar: 'Аватар',
    biography: 'Биография',
    biographyIntro: 'Напишите начальную историю жизни мемориала. Ничто не станет памятью аватара, пока вы явно не запустите индексацию.',
    biographyPlaceholder: 'Напишите биографию здесь...',
    biographySave: 'Сохранить биографию',
    biographyStartIngestion: 'Запустить индексацию',
    biographyConfirmNote: 'После индексации аватар сможет использовать эту биографию в своих ответах.',
    biographyStatusDraft: 'Черновик - ещё не проиндексировано',
    biographyStatusReady: 'В очереди на индексацию',
    biographyStatusIngesting: 'Идёт индексация...',
    biographyStatusIndexed: 'Проиндексировано - часть памяти аватара',
    biographyStatusFailed: 'Индексация не удалась',
    biographyStatusStale: 'Изменено после последней индексации - запустите индексацию заново',
    biographyRetry: 'Повторить индексацию',
    biographer: 'ИИ-биограф',
    biographerIntro: 'ИИ-биограф задаёт по одному вопросу, чтобы больше узнать об этом человеке. Ответы никогда не индексируются автоматически - они проходят ту же проверку, что и любой другой вклад.',
    biographerBlockedMissing: 'Сначала сохраните биографию.',
    biographerBlockedNotIndexed: 'Сначала проиндексируйте биографию, прежде чем запускать биографа.',
    biographerBlockedActive: 'Пожалуйста, сначала ответьте на текущий уточняющий вопрос ниже.',
    biographerDone: 'Все темы ИИ-биографа для этого мемориала уже пройдены.',
    biographerAnswerPlaceholder: 'Напишите свой ответ...',
    biographerSubmit: 'Отправить ответ',
    biographerSkip: 'Пропустить вопрос',
    candidatesTitle: 'Воспоминания от биографа',
    candidatesEmpty: 'Пока нет воспоминаний от ИИ-биографа.',
    candidateConfirm: 'Подтвердить',
    candidateReject: 'Отклонить',
    candidateRequestDetails: 'Запросить больше деталей',
    candidateMarkDisputed: 'Отметить как спорное',
    candidateIndexButton: 'Проиндексировать воспоминание',
    candidateIndexedLabel: 'Проиндексировано и доступно для поиска',
    candidatePendingIndexLabel: 'Одобрено, ещё не проиндексировано',
    candidateClarificationPending: 'Биографу нужна ещё одна деталь, прежде чем это можно будет проверить:',
    candidateClarificationPlaceholder: 'Напишите свой ответ...',
    candidateClarificationSubmit: 'Отправить',
    createMemorial: 'Создать мемориал',
    name: 'Имя',
    description: 'Описание',
    yourMemorials: 'Ваши мемориалы',
    empty: 'Для этого аккаунта пока нет мемориалов.',
    openWorkspace: 'Открыть workspace',
    overview: 'Обзор',
    contributions: 'Воспоминания',
    review: 'Проверка',
    members: 'Участники',
    invitations: 'Приглашения',
    role: 'Роль',
    submitMemory: 'Добавить воспоминание',
    titleLabel: 'Название',
    memoryText: 'Текст воспоминания',
    sourceNote: 'Источник',
    privacyScope: 'Приватность',
    submitForReview: 'Отправить на проверку',
    viewerReadOnly: 'Viewer не может добавлять воспоминания.',
    noContributions: 'Для этой роли нет видимых воспоминаний.',
    notActiveMemory: 'Не активная память',
    activeMemory: 'Подходит для активной памяти',
    noPending: 'Нет записей на проверке.',
    approve: 'Одобрить',
    reject: 'Отклонить',
    archive: 'Архивировать',
    inviteParticipant: 'Пригласить участника',
    inviteHelp: 'Владелец может пригласить trusted reviewer, contributor или viewer.',
    invitationCreated: 'Приглашение создано.',
    devToken: 'Dev invite token',
    tokenNote: 'Показан потому, что backend возвращает его для dev/test flow. Он не сохраняется в browser storage.',
    acceptTitle: 'Принять приглашение',
    acceptHelp: 'Войдите под приглашенным аккаунтом. Token используется один раз из URL.',
    acceptInvitation: 'Принять приглашение',
    invitationAccepted: 'Приглашение принято.',
    noToken: 'Token приглашения отсутствует.',
    creating: 'Создаю',
    submitting: 'Отправляю',
    working: 'Выполняю',
    indexingPending: 'Одобрено, ожидает индексации',
    indexingIndexed: 'Проиндексировано и доступно для поиска',
    indexingFailed: 'Индексация не удалась',
    indexingRetired: 'Больше не активное знание',
    backToSite: 'Вернуться на сайт'
  }
};

const INVITE_ROLES: InvitableMemorialRole[] = ['trusted_reviewer', 'contributor', 'viewer'];
const PRIVACY_SCOPES: PrivacyScope[] = ['private_owner', 'selected_family', 'all_family', 'public_legacy'];

function normalizeEmail(value: string): string {
  return value.trim().toLowerCase();
}

function safeError(error: unknown): string {
  return error instanceof MemorialApiError ? error.detail : 'The action could not be completed.';
}

function roleLabel(value: string): string {
  return value.replace(/_/g, ' ');
}

function formatDate(value: string | null, lang: Lang): string {
  if (!value) return '-';
  const locale = lang === 'cs' ? 'cs-CZ' : lang === 'ru' ? 'ru-RU' : 'en-US';
  return new Intl.DateTimeFormat(locale).format(new Date(value));
}

function getInvitationTokenFromUrl(): string | null {
  const params = new URLSearchParams(window.location.search);
  return params.get('token');
}

export default function MemorialWorkspace({ lang }: { lang: Lang }) {
  const t = COPY[lang];
  const [session, setSession] = useState<AuthSession | null>(null);
  const [memorials, setMemorials] = useState<MemorialRead[]>([]);
  const [selected, setSelected] = useState<MemorialRead | null>(null);
  const [members, setMembers] = useState<MembershipRead[]>([]);
  const [contributions, setContributions] = useState<ContributionRead[]>([]);
  const [reviewQueue, setReviewQueue] = useState<ContributionRead[]>([]);
  const [activeTab, setActiveTab] = useState<WorkspaceTab>('overview');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [notice, setNotice] = useState<string | null>(null);
  const [invitationToken, setInvitationToken] = useState<string | null>(null);

  const role = selected?.current_user_role;
  const mayInvite = role ? canInvite(role) : false;
  const mayReview = role ? canReview(role) : false;
  const maySubmit = role ? canSubmitContribution(role) : false;

  const pathname = usePathname();
  const route = parseAppRoute(pathname);

  useEffect(() => {
    const token = getInvitationTokenFromUrl();
    setInvitationToken(token);
    if (token) {
      const url = new URL(window.location.href);
      url.searchParams.delete('token');
      window.history.replaceState({}, document.title, `${url.pathname}${url.search}${url.hash}`);
    }
  }, []);

  const visibleTabs = useMemo(() => {
    const tabs: WorkspaceTab[] = ['overview', 'biography', 'biographer', 'chat', 'contributions', 'review', 'members', 'invitations'];
    return tabs.filter((tab) => {
      if (tab === 'review') return mayReview;
      if (tab === 'members') return mayReview;
      if (tab === 'invitations') return mayInvite;
      if (tab === 'biography') return role === 'owner';
      return true;
    });
  }, [mayInvite, mayReview, role]);

  async function loadMemorials(accessToken = session?.accessToken, options: { resolveBootstrap?: boolean } = {}) {
    if (!accessToken) return;
    setLoading(true);
    setError(null);
    try {
      const memorialList = await listMemorials(accessToken);
      setMemorials(memorialList);
      if (options.resolveBootstrap) {
        await resolveBootstrapSelection(memorialList, accessToken);
      }
    } catch (loadError) {
      setError(safeError(loadError));
      setMemorials([]);
      setSelected(null);
    } finally {
      setLoading(false);
    }
  }

  /**
   * Deterministic zero/one/many bootstrap (Task 65.1B): a route that already
   * names a memorial id wins (deep link / browser back-forward - still
   * re-validated against the authenticated user's memberships by
   * `loadWorkspace` itself, never trusted blindly). Otherwise, exactly one
   * accessible memorial auto-opens; zero memorials leaves the onboarding
   * create-form visible; more than one leaves the explicit selector visible
   * rather than silently picking one.
   */
  async function resolveBootstrapSelection(memorialList: MemorialRead[], accessToken: string) {
    if (route.name === 'app-memorial') {
      await loadWorkspace(route.profileId, accessToken);
      return;
    }
    if (memorialList.length === 1) {
      await loadWorkspace(memorialList[0].id, accessToken);
    }
  }

  async function loadWorkspace(profileId: number, accessToken = session?.accessToken) {
    if (!accessToken) return;
    setLoading(true);
    setError(null);
    setMembers([]);
    setContributions([]);
    setReviewQueue([]);
    try {
      const memorial = await fetchMemorial(accessToken, profileId);
      setSelected(memorial);
      setActiveTab('overview');
      navigate(buildMemorialPath(profileId));
      const [contributionList, memberList, pendingList] = await Promise.all([
        listContributions(accessToken, profileId),
        canReview(memorial.current_user_role) ? listMembers(accessToken, profileId) : Promise.resolve([]),
        canReview(memorial.current_user_role) ? listReviewQueue(accessToken, profileId) : Promise.resolve([])
      ]);
      setContributions(contributionList);
      setMembers(memberList);
      setReviewQueue(pendingList);
    } catch (loadError) {
      // A stale or unauthorized route memorial id must never render cached
      // private data - clear the active memorial and send the URL back to
      // the selector/onboarding root rather than leaving a dead deep link.
      setSelected(null);
      setMembers([]);
      setContributions([]);
      setReviewQueue([]);
      setError(safeError(loadError));
      navigate(APP_ROOT_PATH);
    } finally {
      setLoading(false);
    }
  }

  function onAuthenticated(nextSession: AuthSession) {
    setSession(nextSession);
    void loadMemorials(nextSession.accessToken, { resolveBootstrap: true });
  }

  function signOut() {
    setSession(null);
    setMemorials([]);
    setSelected(null);
    setMembers([]);
    setContributions([]);
    setReviewQueue([]);
    setNotice(null);
    setError(null);
    // Clear the active-memorial URL too, so a subsequently logged-in user
    // (same browser tab) never lands back on the previous user's deep link.
    navigate(APP_ROOT_PATH);
  }

  return (
    <section id="memorial-workspace" className="relative overflow-hidden px-4 py-24 sm:px-6">
      <div className="absolute inset-0 bg-[radial-gradient(ellipse_70%_45%_at_50%_5%,rgba(127,216,247,.16),transparent_70%),radial-gradient(ellipse_45%_35%_at_100%_40%,rgba(139,124,246,.16),transparent_70%)]" />
      <div className="relative mx-auto max-w-7xl">
        <div className="mx-auto mb-10 max-w-3xl text-center">
          <div className="mb-4 text-xs uppercase tracking-[.34em] text-cyan/65">{t.kicker}</div>
          <h2 className="font-serif text-[clamp(34px,5vw,68px)] leading-[1.05] text-balance">{t.title}</h2>
          <p className="mx-auto mt-5 max-w-2xl text-sm leading-7 text-fg/62 sm:text-base">{t.subtitle}</p>
        </div>

        {invitationToken && (
          <InvitationAcceptPanel
            invitationToken={invitationToken}
            lang={lang}
            onAccepted={(membership) => {
              setNotice(t.invitationAccepted);
              setInvitationToken(null);
              if (session) void loadMemorials(session.accessToken);
              if (membership.profile_id && session) void loadWorkspace(membership.profile_id, session.accessToken);
            }}
            onAuthenticated={onAuthenticated}
            session={session}
            t={t}
          />
        )}

        {!session ? (
          invitationToken ? null : (
          <AuthPanel onAuthenticated={onAuthenticated} t={t} />
          )
        ) : (
          <div className="space-y-5">
            <section className="rounded-[28px] border border-white/10 bg-white/[.045] p-4 shadow-[0_24px_80px_rgba(0,0,0,.28)] backdrop-blur sm:p-5">
              <div className="flex min-w-0 flex-col gap-4 sm:flex-row sm:items-center sm:justify-between">
                <div className="min-w-0">
                  <p className="text-xs uppercase tracking-[.22em] text-fg/40">{t.signedInAs}</p>
                  <strong className="block truncate text-sm text-fg sm:text-base">{session.email}</strong>
                </div>
                <div className="grid grid-cols-2 gap-2 sm:flex sm:justify-end">
                  <button className="rounded-full border border-white/15 px-4 py-2.5 text-sm text-fg/75 transition hover:bg-white/10" onClick={() => void loadMemorials()} type="button">
                    {t.refresh}
                  </button>
                  <button className="rounded-full border border-white/15 px-4 py-2.5 text-sm text-fg/75 transition hover:bg-white/10" onClick={signOut} type="button">
                    {t.signOut}
                  </button>
                </div>
              </div>
            </section>

            {error && <p className="rounded-2xl border border-red-400/30 bg-red-500/10 px-4 py-3 text-sm text-red-100">{error}</p>}
            {notice && <p className="rounded-2xl border border-cyan/30 bg-cyan/10 px-4 py-3 text-sm text-cyan">{notice}</p>}

            <div className="grid min-w-0 gap-5 lg:grid-cols-[minmax(0,0.88fr)_minmax(0,1.12fr)]">
              <CreateMemorialForm
                onCreated={(memorial) => {
                  setMemorials((items) => [memorial, ...items.filter((item) => item.id !== memorial.id)]);
                  void loadWorkspace(memorial.id);
                }}
                t={t}
                token={session.accessToken}
              />
              <MemorialList
                loading={loading && !selected}
                memorials={memorials}
                onOpen={(profileId) => void loadWorkspace(profileId)}
                t={t}
                lang={lang}
              />
            </div>

            {selected && (
              <section className="grid min-w-0 gap-5 rounded-[34px] border border-white/10 bg-black/20 p-3 sm:p-4 lg:grid-cols-[280px_minmax(0,1fr)]">
                <aside className="min-w-0 rounded-[28px] border border-white/10 bg-white/[.045] p-4 sm:p-5">
                  <p className="mb-3 text-xs uppercase tracking-[.24em] text-cyan/60">{t.openWorkspace}</p>
                  <h3 className="break-words font-serif text-3xl leading-tight">{selected.name}</h3>
                  <p className="mt-2 text-sm text-fg/55">
                    {t.role}: {roleLabel(selected.current_user_role)}
                  </p>
                  <div className="mt-6 grid gap-2" role="tablist" aria-label="Workspace sections">
                    {visibleTabs.map((tab) => (
                      <button
                        aria-selected={activeTab === tab}
                        className={`min-w-0 rounded-2xl px-4 py-3 text-left text-sm transition ${
                          activeTab === tab ? 'bg-cyan/18 text-cyan shadow-[0_0_24px_rgba(127,216,247,.14)]' : 'bg-white/[.045] text-fg/65 hover:bg-white/[.08]'
                        }`}
                        key={tab}
                        onClick={() => setActiveTab(tab)}
                        role="tab"
                        type="button"
                      >
                        {t[tab]}
                      </button>
                    ))}
                  </div>
                </aside>

                <div className="min-w-0 rounded-[28px] border border-white/10 bg-white/[.045] p-4 sm:p-6">
                  {activeTab === 'overview' && <Overview memorial={selected} t={t} lang={lang} />}
                  {activeTab === 'biography' && role === 'owner' && (
                    <BiographyPanel profileId={selected.id} t={t} token={session.accessToken} />
                  )}
                  {activeTab === 'biographer' && (
                    <BiographerPanel profileId={selected.id} t={t} token={session.accessToken} />
                  )}
                  {activeTab === 'chat' && <ChatPanel profileId={selected.id} t={t} token={session.accessToken} />}
                  {activeTab === 'contributions' && (
                    <ContributionsSection
                      contributions={contributions}
                      lang={lang}
                      maySubmit={maySubmit}
                      onSubmitted={(contribution) => {
                        setContributions((items) => [contribution, ...items]);
                        if (mayReview && contribution.status === 'needs_review') {
                          setReviewQueue((items) => [contribution, ...items]);
                        }
                        setNotice(t.submitting);
                      }}
                      profileId={selected.id}
                      t={t}
                      token={session.accessToken}
                    />
                  )}
                  {activeTab === 'review' && mayReview && (
                    <ReviewQueue
                      lang={lang}
                      onReviewed={(updated) => {
                        setReviewQueue((items) => items.filter((item) => item.id !== updated.id));
                        setContributions((items) =>
                          items.map((item) =>
                            item.id === updated.id
                              ? updated
                              : updated.supersedes_contribution_id === item.id
                                ? { ...item, status: 'superseded', is_current: false, active_memory_eligible: false }
                                : item
                          )
                        );
                        setNotice(`${t.review}: ${updated.status}.`);
                      }}
                      profileId={selected.id}
                      queue={reviewQueue}
                      t={t}
                      token={session.accessToken}
                    />
                  )}
                  {activeTab === 'review' && mayReview && (
                    <div className="mt-8 border-t border-white/10 pt-8">
                      <CandidatesReviewSection
                        isOwner={role === 'owner'}
                        profileId={selected.id}
                        t={t}
                        token={session.accessToken}
                      />
                    </div>
                  )}
                  {activeTab === 'members' && mayReview && <MembersSection members={members} t={t} />}
                  {activeTab === 'invitations' && mayInvite && (
                    <InvitationSection
                      onInvited={() => setNotice(t.invitationCreated)}
                      profileId={selected.id}
                      t={t}
                      token={session.accessToken}
                    />
                  )}
                </div>
              </section>
            )}
          </div>
        )}
      </div>
    </section>
  );
}

function AuthPanel({ t, onAuthenticated }: { t: Copy; onAuthenticated: (session: AuthSession) => void }) {
  const [mode, setMode] = useState<'login' | 'register'>('login');
  const [email, setEmail] = useState('');
  const [fullName, setFullName] = useState('');
  const [password, setPassword] = useState('');
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function submit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    const normalizedEmail = normalizeEmail(email);
    if (!normalizedEmail.includes('@')) {
      setError('Enter a valid email address.');
      return;
    }
    if (password.length < 8) {
      setError('Password must have at least 8 characters.');
      return;
    }

    setBusy(true);
    setError(null);
    try {
      if (mode === 'register') await register(normalizedEmail, password, fullName.trim() || null);
      const accessToken = await login(normalizedEmail, password);
      setPassword('');
      onAuthenticated({ accessToken, email: normalizedEmail });
    } catch (authError) {
      setError(safeError(authError));
    } finally {
      setBusy(false);
    }
  }

  return (
    <section className="mx-auto max-w-2xl rounded-[34px] border border-white/10 bg-white/[.045] p-5 shadow-[0_24px_80px_rgba(0,0,0,.32)] backdrop-blur sm:p-7">
      <p className="text-xs uppercase tracking-[.26em] text-cyan/60">{t.signInTitle}</p>
      <p className="mt-3 text-sm leading-6 text-fg/60">{t.signInHelp}</p>
      <div className="mt-6 grid grid-cols-2 gap-2 rounded-full border border-white/10 bg-black/20 p-1">
        <button className={`rounded-full px-4 py-2.5 text-sm ${mode === 'login' ? 'bg-cyan/20 text-cyan' : 'text-fg/55'}`} onClick={() => setMode('login')} type="button">
          {t.signIn}
        </button>
        <button className={`rounded-full px-4 py-2.5 text-sm ${mode === 'register' ? 'bg-cyan/20 text-cyan' : 'text-fg/55'}`} onClick={() => setMode('register')} type="button">
          {t.createAccount}
        </button>
      </div>
      <form className="mt-5 grid gap-4" onSubmit={submit}>
        <Field label={t.email} value={email} onChange={setEmail} type="email" required />
        {mode === 'register' && <Field label={t.fullName} value={fullName} onChange={setFullName} />}
        <Field label={t.password} value={password} onChange={setPassword} type="password" required />
        {error && <p className="rounded-2xl border border-red-400/30 bg-red-500/10 px-4 py-3 text-sm text-red-100">{error}</p>}
        <button className="rounded-full bg-gradient-to-r from-cyan to-violet px-6 py-3.5 text-sm font-semibold text-ink disabled:opacity-55" disabled={busy} type="submit">
          {busy ? t.working : mode === 'login' ? t.signIn : t.createAccount}
        </button>
      </form>
    </section>
  );
}

function InvitationAcceptPanel({
  invitationToken,
  lang,
  onAccepted,
  onAuthenticated,
  session,
  t
}: {
  invitationToken: string;
  lang: Lang;
  onAccepted: (membership: MembershipRead) => void;
  onAuthenticated: (session: AuthSession) => void;
  session: AuthSession | null;
  t: Copy;
}) {
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function accept() {
    if (!session) {
      setError(t.signInTitle);
      return;
    }
    setBusy(true);
    setError(null);
    try {
      onAccepted(await acceptInvitation(session.accessToken, invitationToken));
    } catch (acceptError) {
      setError(safeError(acceptError));
    } finally {
      setBusy(false);
    }
  }

  return (
    <section className="mb-5 grid gap-4 rounded-[30px] border border-cyan/20 bg-cyan/10 p-4 sm:p-6 lg:grid-cols-[minmax(0,1fr)_minmax(280px,420px)]">
      <div className="min-w-0">
        <p className="text-xs uppercase tracking-[.24em] text-cyan/70">{t.acceptTitle}</p>
        <p className="mt-3 text-sm leading-6 text-fg/65">{t.acceptHelp}</p>
        {error && <p className="mt-4 rounded-2xl border border-red-400/30 bg-red-500/10 px-4 py-3 text-sm text-red-100">{error}</p>}
        {session && (
          <button className="mt-5 w-full rounded-full bg-gradient-to-r from-cyan to-violet px-6 py-3.5 text-sm font-semibold text-ink disabled:opacity-55 sm:w-auto" disabled={busy} onClick={accept} type="button">
            {busy ? t.working : t.acceptInvitation}
          </button>
        )}
      </div>
      {!session && <AuthPanel onAuthenticated={onAuthenticated} t={t} />}
      {session && <p className="self-center rounded-2xl border border-white/10 bg-black/20 p-4 text-sm text-fg/65">{formatDate(new Date().toISOString(), lang)}</p>}
    </section>
  );
}

function CreateMemorialForm({ token, t, onCreated }: { token: string; t: Copy; onCreated: (memorial: MemorialRead) => void }) {
  const [name, setName] = useState('');
  const [biography, setBiography] = useState('');
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function submit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    if (name.trim().length < 2) {
      setError('Memorial name is required.');
      return;
    }
    setBusy(true);
    setError(null);
    try {
      const memorial = await createMemorial(token, { name: name.trim(), biography: biography.trim() || null });
      setName('');
      setBiography('');
      onCreated(memorial);
    } catch (createError) {
      setError(safeError(createError));
    } finally {
      setBusy(false);
    }
  }

  return (
    <section className="min-w-0 rounded-[28px] border border-white/10 bg-white/[.045] p-4 sm:p-6">
      <h3 className="font-serif text-3xl">{t.createMemorial}</h3>
      <form className="mt-5 grid gap-4" onSubmit={submit}>
        <Field label={t.name} value={name} onChange={setName} required />
        <Textarea label={t.description} value={biography} onChange={setBiography} />
        {error && <p className="rounded-2xl border border-red-400/30 bg-red-500/10 px-4 py-3 text-sm text-red-100">{error}</p>}
        <button className="rounded-full bg-gradient-to-r from-cyan to-violet px-6 py-3.5 text-sm font-semibold text-ink disabled:opacity-55" disabled={busy} type="submit">
          {busy ? t.creating : t.createMemorial}
        </button>
      </form>
    </section>
  );
}

function MemorialList({
  loading,
  memorials,
  onOpen,
  t,
  lang
}: {
  loading: boolean;
  memorials: MemorialRead[];
  onOpen: (profileId: number) => void;
  t: Copy;
  lang: Lang;
}) {
  return (
    <section className="min-w-0 rounded-[28px] border border-white/10 bg-white/[.045] p-4 sm:p-6">
      <div className="flex items-center justify-between gap-3">
        <h3 className="font-serif text-3xl">{t.yourMemorials}</h3>
        {loading && <span className="rounded-full bg-white/10 px-3 py-1 text-xs text-fg/55">{t.working}</span>}
      </div>
      {!loading && memorials.length === 0 && <p className="mt-5 text-sm leading-6 text-fg/58">{t.empty}</p>}
      <div className="mt-5 grid gap-3">
        {memorials.map((memorial) => (
          <article className="min-w-0 rounded-3xl border border-white/10 bg-black/20 p-4" key={memorial.id}>
            <div className="flex min-w-0 flex-col gap-3 sm:flex-row sm:items-start sm:justify-between">
              <div className="min-w-0">
                <h4 className="break-words text-lg font-semibold">{memorial.name}</h4>
                <p className="mt-2 line-clamp-3 text-sm leading-6 text-fg/55">{memorial.biography || t.description}</p>
                <p className="mt-2 text-xs text-fg/38">{formatDate(memorial.created_at, lang)}</p>
              </div>
              <span className="w-fit rounded-full bg-white/10 px-3 py-1 text-xs text-cyan">{roleLabel(memorial.current_user_role)}</span>
            </div>
            <button className="mt-4 w-full rounded-full border border-white/15 px-4 py-3 text-sm text-fg/75 transition hover:bg-white/10 sm:w-auto" onClick={() => onOpen(memorial.id)} type="button">
              {t.openWorkspace}
            </button>
          </article>
        ))}
      </div>
    </section>
  );
}

function Overview({ memorial, t, lang }: { memorial: MemorialRead; t: Copy; lang: Lang }) {
  return (
    <div className="min-w-0 space-y-5">
      <h3 className="font-serif text-3xl">{t.overview}</h3>
      <p className="break-words text-sm leading-7 text-fg/65">{memorial.biography || t.empty}</p>
      <div className="flex flex-wrap gap-2">
        <Badge>{t.role}: {roleLabel(memorial.current_user_role)}</Badge>
        <Badge>{formatDate(memorial.created_at, lang)}</Badge>
      </div>
    </div>
  );
}

function ChatPanel({ token, profileId, t }: { token: string; profileId: number; t: Copy }) {
  const [messages, setMessages] = useState<ChatMessageRead[]>([]);
  const [text, setText] = useState('');
  const [loading, setLoading] = useState(true);
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    let cancelled = false;
    setLoading(true);
    setError(null);
    listChatMessages(token, profileId)
      .then((history) => {
        if (!cancelled) setMessages(history);
      })
      .catch((loadError) => {
        if (!cancelled) setError(safeError(loadError));
      })
      .finally(() => {
        if (!cancelled) setLoading(false);
      });
    return () => {
      cancelled = true;
    };
  }, [token, profileId]);

  async function submit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    const trimmed = text.trim();
    if (!trimmed) return;
    setBusy(true);
    setError(null);
    const optimisticUserMessage: ChatMessageRead = {
      id: -Date.now(),
      profile_id: profileId,
      role: 'user',
      content: trimmed,
      created_at: new Date().toISOString()
    };
    setMessages((items) => [...items, optimisticUserMessage]);
    setText('');
    try {
      const response = await sendChatMessage(token, profileId, trimmed);
      setMessages((items) => [
        ...items.filter((item) => item.id !== optimisticUserMessage.id),
        { id: response.message_id - 1, profile_id: response.profile_id, role: 'user', content: response.user_message, created_at: response.created_at },
        { id: response.message_id, profile_id: response.profile_id, role: 'assistant', content: response.ai_response_text, created_at: response.created_at }
      ]);
    } catch (sendError) {
      setMessages((items) => items.filter((item) => item.id !== optimisticUserMessage.id));
      setText(trimmed);
      setError(safeError(sendError));
    } finally {
      setBusy(false);
    }
  }

  return (
    <div className="min-w-0 space-y-5">
      <h3 className="font-serif text-3xl">{t.chat}</h3>
      <div className="min-w-0 space-y-3 rounded-3xl border border-white/10 bg-black/20 p-4">
        {loading && <p className="text-sm text-fg/55">{t.working}</p>}
        {!loading && messages.length === 0 && <p className="text-sm text-fg/60">{t.chatEmpty}</p>}
        {messages.map((message) => (
          <div className={`min-w-0 ${message.role === 'assistant' ? '' : 'text-right'}`} key={message.id}>
            <p className="text-xs uppercase tracking-[.18em] text-fg/38">
              {message.role === 'assistant' ? t.chatAvatar : t.chatYou}
            </p>
            <p
              className={`mt-1 inline-block max-w-full whitespace-pre-wrap break-words rounded-2xl px-4 py-2.5 text-left text-sm leading-6 ${
                message.role === 'assistant' ? 'bg-white/[.06] text-fg/85' : 'bg-cyan/15 text-fg'
              }`}
            >
              {message.content}
            </p>
          </div>
        ))}
      </div>
      {error && <p className="rounded-2xl border border-red-400/30 bg-red-500/10 px-4 py-3 text-sm text-red-100">{error}</p>}
      <form className="flex min-w-0 flex-col gap-3 sm:flex-row" onSubmit={submit}>
        <input
          className="min-w-0 flex-1 rounded-2xl border border-white/10 bg-black/25 px-4 py-3 text-fg outline-none transition placeholder:text-fg/30 focus:border-cyan/70"
          maxLength={4000}
          onChange={(event) => setText(event.target.value)}
          placeholder={t.chatPlaceholder}
          value={text}
        />
        <button className="shrink-0 rounded-full bg-gradient-to-r from-cyan to-violet px-6 py-3 text-sm font-semibold text-ink disabled:opacity-55" disabled={busy || !text.trim()} type="submit">
          {busy ? t.working : t.chatSend}
        </button>
      </form>
    </div>
  );
}

const BIOGRAPHY_POLL_INTERVAL_MS = 3000;
const BIOGRAPHY_TERMINAL_STATUSES = new Set(['indexed', 'failed', 'stale', 'draft']);

function biographyStatusLabel(t: Copy, status: BiographyStatusRead['status']): string {
  switch (status) {
    case 'draft':
      return t.biographyStatusDraft;
    case 'ready_for_ingestion':
      return t.biographyStatusReady;
    case 'ingesting':
      return t.biographyStatusIngesting;
    case 'indexed':
      return t.biographyStatusIndexed;
    case 'failed':
      return t.biographyStatusFailed;
    case 'stale':
      return t.biographyStatusStale;
    default:
      return status;
  }
}

function BiographyPanel({ token, profileId, t }: { token: string; profileId: number; t: Copy }) {
  const [text, setText] = useState('');
  const [status, setStatus] = useState<BiographyStatusRead | null>(null);
  const [loading, setLoading] = useState(true);
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    let cancelled = false;
    let timer: ReturnType<typeof setTimeout> | null = null;

    async function poll() {
      try {
        const next = await getBiographyStatus(token, profileId);
        if (cancelled) return;
        setStatus(next);
        setLoading(false);
        if (!BIOGRAPHY_TERMINAL_STATUSES.has(next.status) || next.status === 'ready_for_ingestion') {
          timer = setTimeout(poll, BIOGRAPHY_POLL_INTERVAL_MS);
        }
      } catch (loadError) {
        if (!cancelled) {
          setError(safeError(loadError));
          setLoading(false);
        }
      }
    }

    void poll();
    return () => {
      cancelled = true;
      if (timer) clearTimeout(timer);
    };
  }, [token, profileId]);

  async function save() {
    setBusy(true);
    setError(null);
    try {
      const next = await updateBiography(token, profileId, text);
      setStatus(next);
    } catch (saveError) {
      setError(safeError(saveError));
    } finally {
      setBusy(false);
    }
  }

  async function startIngestion() {
    setBusy(true);
    setError(null);
    try {
      const next = await startBiographyIngestion(token, profileId);
      setStatus(next);
    } catch (startError) {
      setError(safeError(startError));
    } finally {
      setBusy(false);
    }
  }

  const canStart = status !== null && text.trim().length >= 2 && status.status !== 'ingesting';

  return (
    <div className="min-w-0 space-y-5">
      <div>
        <h3 className="font-serif text-3xl">{t.biography}</h3>
        <p className="mt-2 text-sm leading-6 text-fg/58">{t.biographyIntro}</p>
      </div>
      {loading && <p className="text-sm text-fg/55">{t.working}</p>}
      {status && (
        <div className="flex flex-wrap items-center gap-2">
          <Badge tone={status.status === 'indexed' ? 'cyan' : status.status === 'failed' ? 'danger' : 'muted'}>
            {biographyStatusLabel(t, status.status)}
          </Badge>
          {status.background_job_status && <Badge>{status.background_job_status}</Badge>}
        </div>
      )}
      <Textarea label={t.name} value={text} onChange={setText} required maxLength={20000} />
      <p className="text-xs text-fg/45">{t.biographyConfirmNote}</p>
      {error && <p className="rounded-2xl border border-red-400/30 bg-red-500/10 px-4 py-3 text-sm text-red-100">{error}</p>}
      <div className="flex flex-wrap gap-3">
        <button
          className="rounded-full border border-white/15 px-5 py-3 text-sm text-fg/75 transition hover:bg-white/10 disabled:opacity-55"
          disabled={busy || text.trim().length < 2}
          onClick={() => void save()}
          type="button"
        >
          {busy ? t.working : t.biographySave}
        </button>
        <button
          className="rounded-full bg-gradient-to-r from-cyan to-violet px-5 py-3 text-sm font-semibold text-ink disabled:opacity-55"
          disabled={busy || !canStart}
          onClick={() => void startIngestion()}
          type="button"
        >
          {busy ? t.working : status?.status === 'failed' || status?.status === 'stale' ? t.biographyRetry : t.biographyStartIngestion}
        </button>
      </div>
    </div>
  );
}

function BiographerPanel({ token, profileId, t }: { token: string; profileId: number; t: Copy }) {
  const [eligibility, setEligibility] = useState<BiographerEligibilityRead | null>(null);
  const [question, setQuestion] = useState<BiographerQuestionRead | null>(null);
  const [activeCandidateId, setActiveCandidateId] = useState<number | null>(null);
  const [answerText, setAnswerText] = useState('');
  const [loading, setLoading] = useState(true);
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [done, setDone] = useState(false);

  const lang: 'cs' | 'ru' = 'cs';

  async function load() {
    setLoading(true);
    setError(null);
    setDone(false);
    try {
      const nextEligibility = await getBiographerEligibility(token, profileId);
      setEligibility(nextEligibility);
      if (nextEligibility.eligible) {
        const nextQuestion = await getNextBiographerQuestion(token, profileId, lang);
        setQuestion(nextQuestion);
        setDone(nextQuestion === null);
      } else {
        setQuestion(null);
      }
    } catch (loadError) {
      setError(safeError(loadError));
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    void load();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [token, profileId]);

  async function submitAnswer(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    if (!question || !answerText.trim()) return;
    setBusy(true);
    setError(null);
    try {
      const response = await answerBiographerQuestion(token, profileId, question.id, lang, answerText.trim());
      setAnswerText('');
      if (response.unresolved_clarification_count && response.unresolved_clarification_count > 0 && response.candidate_id) {
        setActiveCandidateId(response.candidate_id);
        setQuestion(null);
      } else {
        setActiveCandidateId(null);
        await load();
      }
    } catch (answerError) {
      setError(safeError(answerError));
    } finally {
      setBusy(false);
    }
  }

  async function submitClarification(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    if (!activeCandidateId || !answerText.trim()) return;
    setBusy(true);
    setError(null);
    try {
      const enrichment = await answerCandidateClarification(token, profileId, activeCandidateId, answerText.trim());
      setAnswerText('');
      if (enrichment.unresolved_clarification_count === 0) {
        setActiveCandidateId(null);
        await load();
      }
    } catch (clarificationError) {
      setError(safeError(clarificationError));
    } finally {
      setBusy(false);
    }
  }

  async function skip() {
    if (!question) return;
    setBusy(true);
    setError(null);
    try {
      await skipBiographerQuestion(token, profileId, question.id);
      await load();
    } catch (skipError) {
      setError(safeError(skipError));
    } finally {
      setBusy(false);
    }
  }

  return (
    <div className="min-w-0 space-y-5">
      <div>
        <h3 className="font-serif text-3xl">{t.biographer}</h3>
        <p className="mt-2 text-sm leading-6 text-fg/58">{t.biographerIntro}</p>
      </div>
      {loading && <p className="text-sm text-fg/55">{t.working}</p>}
      {error && <p className="rounded-2xl border border-red-400/30 bg-red-500/10 px-4 py-3 text-sm text-red-100">{error}</p>}
      {!loading && eligibility && !eligibility.eligible && (
        <p className="rounded-2xl border border-white/10 bg-black/20 p-4 text-sm text-fg/60">
          {eligibility.blocked_reason === 'biography_missing' && t.biographerBlockedMissing}
          {eligibility.blocked_reason === 'biography_not_indexed' && t.biographerBlockedNotIndexed}
          {eligibility.blocked_reason === 'active_candidate_requires_answer' && t.biographerBlockedActive}
        </p>
      )}
      {!loading && activeCandidateId && (
        <form className="grid gap-4 rounded-3xl border border-cyan/20 bg-cyan/10 p-4" onSubmit={(event) => void submitClarification(event)}>
          <p className="text-sm leading-6 text-fg/75">{t.candidateClarificationPending}</p>
          <Textarea label={t.candidateClarificationPlaceholder} value={answerText} onChange={setAnswerText} required maxLength={1000} />
          <button className="rounded-full bg-gradient-to-r from-cyan to-violet px-6 py-3 text-sm font-semibold text-ink disabled:opacity-55" disabled={busy || !answerText.trim()} type="submit">
            {busy ? t.working : t.candidateClarificationSubmit}
          </button>
        </form>
      )}
      {!loading && !activeCandidateId && eligibility?.eligible && question && (
        <form className="grid gap-4 rounded-3xl border border-white/10 bg-black/20 p-4" onSubmit={(event) => void submitAnswer(event)}>
          <p className="text-lg font-semibold text-fg">{question.question_text}</p>
          <Textarea label={t.biographerAnswerPlaceholder} value={answerText} onChange={setAnswerText} required maxLength={2000} />
          <div className="flex flex-wrap gap-3">
            <button className="rounded-full bg-gradient-to-r from-cyan to-violet px-6 py-3 text-sm font-semibold text-ink disabled:opacity-55" disabled={busy || !answerText.trim()} type="submit">
              {busy ? t.working : t.biographerSubmit}
            </button>
            <button
              className="rounded-full border border-white/15 px-6 py-3 text-sm text-fg/75 transition hover:bg-white/10 disabled:opacity-55"
              disabled={busy}
              onClick={() => void skip()}
              type="button"
            >
              {t.biographerSkip}
            </button>
          </div>
        </form>
      )}
      {!loading && !activeCandidateId && eligibility?.eligible && done && (
        <p className="rounded-2xl border border-white/10 bg-black/20 p-4 text-sm text-fg/60">{t.biographerDone}</p>
      )}
    </div>
  );
}

function CandidatesReviewSection({
  token,
  profileId,
  t,
  isOwner
}: {
  token: string;
  profileId: number;
  t: Copy;
  isOwner: boolean;
}) {
  const [candidates, setCandidates] = useState<MemoryCandidateEnrichmentRead[]>([]);
  const [loading, setLoading] = useState(true);
  const [busyId, setBusyId] = useState<number | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [clarificationDrafts, setClarificationDrafts] = useState<Record<number, string>>({});

  async function load() {
    setLoading(true);
    setError(null);
    try {
      setCandidates(await listMemoryCandidates(token, profileId));
    } catch (loadError) {
      setError(safeError(loadError));
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    void load();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [token, profileId]);

  async function review(candidateId: number, action: OwnerReviewCandidateAction) {
    setBusyId(candidateId);
    setError(null);
    try {
      const updated = await ownerReviewCandidate(token, profileId, candidateId, action, { privacy_scope: 'all_family' });
      setCandidates((items) => items.map((item) => (item.candidate_id === candidateId ? updated : item)));
    } catch (reviewError) {
      setError(safeError(reviewError));
    } finally {
      setBusyId(null);
    }
  }

  async function answerClarification(candidateId: number) {
    const draft = clarificationDrafts[candidateId]?.trim();
    if (!draft) return;
    setBusyId(candidateId);
    setError(null);
    try {
      const updated = await answerCandidateClarification(token, profileId, candidateId, draft);
      setCandidates((items) => items.map((item) => (item.candidate_id === candidateId ? updated : item)));
      setClarificationDrafts((drafts) => ({ ...drafts, [candidateId]: '' }));
    } catch (clarificationError) {
      setError(safeError(clarificationError));
    } finally {
      setBusyId(null);
    }
  }

  async function indexMemory(candidateId: number) {
    setBusyId(candidateId);
    setError(null);
    try {
      await indexCandidateMemory(token, profileId, candidateId);
      await load();
    } catch (indexError) {
      setError(safeError(indexError));
    } finally {
      setBusyId(null);
    }
  }

  return (
    <div className="min-w-0 space-y-5">
      <h3 className="font-serif text-3xl">{t.candidatesTitle}</h3>
      {loading && <p className="text-sm text-fg/55">{t.working}</p>}
      {error && <p className="rounded-2xl border border-red-400/30 bg-red-500/10 px-4 py-3 text-sm text-red-100">{error}</p>}
      {!loading && candidates.length === 0 && <p className="rounded-2xl border border-white/10 bg-black/20 p-4 text-sm text-fg/60">{t.candidatesEmpty}</p>}
      <div className="grid gap-3">
        {candidates.map((candidate) => (
          <article className="min-w-0 rounded-3xl border border-white/10 bg-black/20 p-4" key={candidate.candidate_id}>
            <p className="break-words text-sm leading-6 text-fg/80">{candidate.finalized_memory_text || '-'}</p>
            <div className="mt-3 flex flex-wrap gap-2">
              <Badge>{candidate.review_status}</Badge>
              {candidate.searchable_as_fact && <Badge tone="cyan">{t.candidateIndexedLabel}</Badge>}
              {candidate.explicit_indexing_required && <Badge tone="muted">{t.candidatePendingIndexLabel}</Badge>}
            </div>

            {candidate.next_clarification_question && (
              <div className="mt-4 grid gap-2 rounded-2xl border border-cyan/20 bg-cyan/10 p-3">
                <p className="text-sm text-fg/75">{candidate.next_clarification_question.question_text}</p>
                <input
                  className="min-w-0 rounded-2xl border border-white/10 bg-black/25 px-4 py-2.5 text-fg outline-none focus:border-cyan/70"
                  onChange={(event) =>
                    setClarificationDrafts((drafts) => ({ ...drafts, [candidate.candidate_id]: event.target.value }))
                  }
                  value={clarificationDrafts[candidate.candidate_id] || ''}
                />
                <button
                  className="w-fit rounded-full border border-white/15 px-4 py-2 text-xs text-fg/75 transition hover:bg-white/10 disabled:opacity-55"
                  disabled={busyId === candidate.candidate_id}
                  onClick={() => void answerClarification(candidate.candidate_id)}
                  type="button"
                >
                  {t.candidateClarificationSubmit}
                </button>
              </div>
            )}

            {candidate.review_status === 'needs_review' && !candidate.next_clarification_question && isOwner && (
              <div className="mt-4 grid gap-2 sm:grid-cols-2 lg:grid-cols-4">
                <ActionButton
                  disabled={busyId === candidate.candidate_id}
                  label={t.candidateConfirm}
                  onClick={() => void review(candidate.candidate_id, 'confirm')}
                  tone="primary"
                />
                <ActionButton
                  disabled={busyId === candidate.candidate_id}
                  label={t.candidateRequestDetails}
                  onClick={() => void review(candidate.candidate_id, 'request_more_details')}
                  tone="secondary"
                />
                <ActionButton
                  disabled={busyId === candidate.candidate_id}
                  label={t.candidateMarkDisputed}
                  onClick={() => void review(candidate.candidate_id, 'mark_disputed')}
                  tone="secondary"
                />
                <ActionButton
                  disabled={busyId === candidate.candidate_id}
                  label={t.candidateReject}
                  onClick={() => void review(candidate.candidate_id, 'reject')}
                  tone="danger"
                />
              </div>
            )}

            {candidate.explicit_indexing_required && isOwner && (
              <div className="mt-4">
                <ActionButton
                  disabled={busyId === candidate.candidate_id}
                  label={t.candidateIndexButton}
                  onClick={() => void indexMemory(candidate.candidate_id)}
                  tone="primary"
                />
              </div>
            )}
          </article>
        ))}
      </div>
    </div>
  );
}

function ContributionsSection({
  contributions,
  lang,
  maySubmit,
  onSubmitted,
  profileId,
  t,
  token
}: {
  contributions: ContributionRead[];
  lang: Lang;
  maySubmit: boolean;
  onSubmitted: (contribution: ContributionRead) => void;
  profileId: number;
  t: Copy;
  token: string;
}) {
  return (
    <div className="min-w-0 space-y-5">
      <div>
        <h3 className="font-serif text-3xl">{t.contributions}</h3>
        <p className="mt-2 text-sm leading-6 text-fg/58">{t.submitMemory}</p>
      </div>
      {maySubmit ? <ContributionForm onSubmitted={onSubmitted} profileId={profileId} t={t} token={token} /> : <p className="rounded-2xl border border-white/10 bg-black/20 p-4 text-sm text-fg/60">{t.viewerReadOnly}</p>}
      <ContributionList contributions={contributions} lang={lang} t={t} />
    </div>
  );
}

function ContributionForm({
  token,
  profileId,
  t,
  onSubmitted
}: {
  token: string;
  profileId: number;
  t: Copy;
  onSubmitted: (contribution: ContributionRead) => void;
}) {
  const [title, setTitle] = useState('');
  const [memoryText, setMemoryText] = useState('');
  const [sourceNote, setSourceNote] = useState('');
  const [privacyScope, setPrivacyScope] = useState<PrivacyScope>('private_owner');
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function submit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    if (!title.trim() || !memoryText.trim()) {
      setError('Title and memory text are required.');
      return;
    }
    setBusy(true);
    setError(null);
    try {
      const contribution = await submitContribution(token, profileId, {
        title: title.trim(),
        memory_text: memoryText.trim(),
        source_note: sourceNote.trim() || null,
        privacy_scope: privacyScope
      });
      setTitle('');
      setMemoryText('');
      setSourceNote('');
      onSubmitted(contribution);
    } catch (submitError) {
      setError(safeError(submitError));
    } finally {
      setBusy(false);
    }
  }

  return (
    <form className="grid gap-4 rounded-3xl border border-white/10 bg-black/20 p-4" onSubmit={submit}>
      <Field label={t.titleLabel} value={title} onChange={setTitle} required maxLength={200} />
      <Textarea label={t.memoryText} value={memoryText} onChange={setMemoryText} required maxLength={5000} />
      <Field label={t.sourceNote} value={sourceNote} onChange={setSourceNote} maxLength={500} />
      <label className="grid gap-2 text-sm text-fg/62">
        <span>{t.privacyScope}</span>
        <select className="min-w-0 rounded-2xl border border-white/10 bg-ink px-4 py-3 text-fg outline-none focus:border-cyan/70" onChange={(event) => setPrivacyScope(event.target.value as PrivacyScope)} value={privacyScope}>
          {PRIVACY_SCOPES.map((scope) => (
            <option key={scope} value={scope}>
              {scope}
            </option>
          ))}
        </select>
      </label>
      {error && <p className="rounded-2xl border border-red-400/30 bg-red-500/10 px-4 py-3 text-sm text-red-100">{error}</p>}
      <button className="rounded-full bg-gradient-to-r from-cyan to-violet px-6 py-3.5 text-sm font-semibold text-ink disabled:opacity-55" disabled={busy} type="submit">
        {busy ? t.submitting : t.submitForReview}
      </button>
    </form>
  );
}

function ContributionList({ contributions, lang, t }: { contributions: ContributionRead[]; lang: Lang; t: Copy }) {
  if (contributions.length === 0) {
    return <p className="rounded-2xl border border-white/10 bg-black/20 p-4 text-sm text-fg/60">{t.noContributions}</p>;
  }
  return (
    <div className="grid min-w-0 gap-3">
      {contributions.map((contribution) => (
        <article className="min-w-0 rounded-3xl border border-white/10 bg-black/20 p-4" key={contribution.id}>
          <div className="flex min-w-0 flex-col gap-3 lg:flex-row lg:items-start lg:justify-between">
            <div className="min-w-0">
              <h4 className="break-words text-lg font-semibold">{contribution.title}</h4>
              <p className="mt-2 break-words text-sm leading-6 text-fg/60">{contribution.memory_text}</p>
              <p className="mt-3 text-xs text-fg/38">
                {contribution.author_email} · {formatDate(contribution.created_at, lang)}
              </p>
              {contribution.rejection_reason && <p className="mt-2 text-sm text-red-100">{contribution.rejection_reason}</p>}
            </div>
            <div className="flex shrink-0 flex-wrap gap-2 lg:justify-end">
              <Badge>{contribution.status}</Badge>
              <Badge tone={isActiveMemoryEligible(contribution) ? 'cyan' : 'muted'}>
                {isActiveMemoryEligible(contribution) ? t.activeMemory : t.notActiveMemory}
              </Badge>
              {indexingStatusLabel(t, contribution.indexing_status.state) && (
                <Badge tone={indexingStatusTone(contribution.indexing_status.state)}>
                  {indexingStatusLabel(t, contribution.indexing_status.state)}
                </Badge>
              )}
            </div>
          </div>
        </article>
      ))}
    </div>
  );
}

function ReviewQueue({
  token,
  profileId,
  queue,
  t,
  lang,
  onReviewed
}: {
  token: string;
  profileId: number;
  queue: ContributionRead[];
  t: Copy;
  lang: Lang;
  onReviewed: (contribution: ContributionRead) => void;
}) {
  const [busyId, setBusyId] = useState<number | null>(null);
  const [error, setError] = useState<string | null>(null);

  async function submitAction(contribution: ContributionRead, action: 'approve' | 'reject' | 'archive') {
    if (!window.confirm(`${action}: ${contribution.title}?`)) return;
    setBusyId(contribution.id);
    setError(null);
    try {
      onReviewed(await reviewContribution(token, profileId, contribution.id, action));
    } catch (reviewError) {
      setError(safeError(reviewError));
    } finally {
      setBusyId(null);
    }
  }

  return (
    <div className="min-w-0 space-y-5">
      <h3 className="font-serif text-3xl">{t.review}</h3>
      {error && <p className="rounded-2xl border border-red-400/30 bg-red-500/10 px-4 py-3 text-sm text-red-100">{error}</p>}
      {queue.length === 0 && <p className="rounded-2xl border border-white/10 bg-black/20 p-4 text-sm text-fg/60">{t.noPending}</p>}
      {queue.map((contribution) => (
        <article className="min-w-0 rounded-3xl border border-white/10 bg-black/20 p-4" key={contribution.id}>
          <h4 className="break-words text-lg font-semibold">{contribution.title}</h4>
          <p className="mt-2 break-words text-sm leading-6 text-fg/60">{contribution.memory_text}</p>
          <p className="mt-3 text-xs text-fg/38">
            {contribution.author_email} · {formatDate(contribution.created_at, lang)}
          </p>
          <div className="mt-4 grid gap-2 sm:grid-cols-3">
            <ActionButton disabled={busyId === contribution.id} label={t.approve} onClick={() => void submitAction(contribution, 'approve')} tone="primary" />
            <ActionButton disabled={busyId === contribution.id} label={t.reject} onClick={() => void submitAction(contribution, 'reject')} tone="secondary" />
            <ActionButton disabled={busyId === contribution.id} label={t.archive} onClick={() => void submitAction(contribution, 'archive')} tone="danger" />
          </div>
        </article>
      ))}
    </div>
  );
}

function MembersSection({ members, t }: { members: MembershipRead[]; t: Copy }) {
  return (
    <div className="min-w-0 space-y-5">
      <h3 className="font-serif text-3xl">{t.members}</h3>
      <div className="grid gap-3">
        {members.map((member) => (
          <article className="flex min-w-0 flex-col gap-2 rounded-3xl border border-white/10 bg-black/20 p-4 sm:flex-row sm:items-center sm:justify-between" key={member.id}>
            <div className="min-w-0">
              <h4 className="truncate text-base font-semibold">{member.email}</h4>
              <p className="text-sm text-fg/45">{member.full_name || '-'}</p>
            </div>
            <Badge>{roleLabel(member.role)}</Badge>
          </article>
        ))}
      </div>
    </div>
  );
}

function InvitationSection({ token, profileId, t, onInvited }: { token: string; profileId: number; t: Copy; onInvited: (invitation: InvitationCreateResponse) => void }) {
  const [email, setEmail] = useState('');
  const [role, setRole] = useState<InvitableMemorialRole>('contributor');
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [lastInvitation, setLastInvitation] = useState<InvitationCreateResponse | null>(null);

  async function submit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    const normalizedEmail = normalizeEmail(email);
    if (!normalizedEmail.includes('@')) {
      setError('Enter a valid email address.');
      return;
    }
    setBusy(true);
    setError(null);
    try {
      const invitation = await inviteParticipant(token, profileId, { email: normalizedEmail, role });
      setLastInvitation(invitation);
      setEmail('');
      onInvited(invitation);
    } catch (inviteError) {
      setError(safeError(inviteError));
    } finally {
      setBusy(false);
    }
  }

  return (
    <div className="min-w-0 space-y-5">
      <div>
        <h3 className="font-serif text-3xl">{t.invitations}</h3>
        <p className="mt-2 text-sm leading-6 text-fg/58">{t.inviteHelp}</p>
      </div>
      <form className="grid gap-4 rounded-3xl border border-white/10 bg-black/20 p-4" onSubmit={submit}>
        <Field label={t.email} value={email} onChange={setEmail} type="email" required />
        <label className="grid gap-2 text-sm text-fg/62">
          <span>{t.role}</span>
          <select className="min-w-0 rounded-2xl border border-white/10 bg-ink px-4 py-3 text-fg outline-none focus:border-cyan/70" onChange={(event) => setRole(event.target.value as InvitableMemorialRole)} value={role}>
            {INVITE_ROLES.map((item) => (
              <option key={item} value={item}>
                {roleLabel(item)}
              </option>
            ))}
          </select>
        </label>
        {error && <p className="rounded-2xl border border-red-400/30 bg-red-500/10 px-4 py-3 text-sm text-red-100">{error}</p>}
        <button className="rounded-full bg-gradient-to-r from-cyan to-violet px-6 py-3.5 text-sm font-semibold text-ink disabled:opacity-55" disabled={busy} type="submit">
          {busy ? t.working : t.inviteParticipant}
        </button>
      </form>
      {lastInvitation?.token && (
        <div className="min-w-0 rounded-3xl border border-cyan/20 bg-cyan/10 p-4">
          <strong className="text-cyan">{t.devToken}</strong>
          <p className="mt-2 text-sm leading-6 text-fg/60">{t.tokenNote}</p>
          <p className="mt-3 break-all rounded-2xl border border-white/10 bg-black/30 p-3 font-mono text-xs text-fg/80">{lastInvitation.token}</p>
        </div>
      )}
    </div>
  );
}

function Field({
  label,
  value,
  onChange,
  type = 'text',
  required = false,
  maxLength
}: {
  label: string;
  value: string;
  onChange: (value: string) => void;
  type?: string;
  required?: boolean;
  maxLength?: number;
}) {
  return (
    <label className="grid min-w-0 gap-2 text-sm text-fg/62">
      <span>{label}</span>
      <input
        className="min-w-0 rounded-2xl border border-white/10 bg-black/25 px-4 py-3 text-fg outline-none transition placeholder:text-fg/30 focus:border-cyan/70"
        maxLength={maxLength}
        onChange={(event) => onChange(event.target.value)}
        required={required}
        type={type}
        value={value}
      />
    </label>
  );
}

function Textarea({
  label,
  value,
  onChange,
  required = false,
  maxLength
}: {
  label: string;
  value: string;
  onChange: (value: string) => void;
  required?: boolean;
  maxLength?: number;
}) {
  return (
    <label className="grid min-w-0 gap-2 text-sm text-fg/62">
      <span>{label}</span>
      <textarea
        className="min-h-28 min-w-0 resize-y rounded-2xl border border-white/10 bg-black/25 px-4 py-3 text-fg outline-none transition placeholder:text-fg/30 focus:border-cyan/70"
        maxLength={maxLength}
        onChange={(event) => onChange(event.target.value)}
        required={required}
        value={value}
      />
    </label>
  );
}

function Badge({ children, tone = 'muted' }: { children: ReactNode; tone?: 'muted' | 'cyan' | 'danger' }) {
  const toneClassName =
    tone === 'cyan' ? 'bg-cyan/15 text-cyan' : tone === 'danger' ? 'bg-red-500/15 text-red-200' : 'bg-white/10 text-fg/62';
  return <span className={`w-fit rounded-full px-3 py-1 text-xs ${toneClassName}`}>{children}</span>;
}

function indexingStatusLabel(t: Copy, state: ContributionRead['indexing_status']['state']): string | null {
  if (state === 'pending') return t.indexingPending;
  if (state === 'indexed') return t.indexingIndexed;
  if (state === 'failed') return t.indexingFailed;
  if (state === 'retired') return t.indexingRetired;
  return null;
}

function indexingStatusTone(state: ContributionRead['indexing_status']['state']): 'cyan' | 'muted' | 'danger' {
  if (state === 'indexed') return 'cyan';
  if (state === 'failed') return 'danger';
  return 'muted';
}

function ActionButton({ disabled, label, onClick, tone }: { disabled: boolean; label: string; onClick: () => void; tone: 'primary' | 'secondary' | 'danger' }) {
  const className =
    tone === 'primary'
      ? 'bg-gradient-to-r from-cyan to-violet text-ink'
      : tone === 'danger'
        ? 'border border-red-300/30 bg-red-500/10 text-red-100'
        : 'border border-white/15 bg-white/[.04] text-fg/75';
  return (
    <button className={`min-w-0 rounded-full px-4 py-3 text-sm font-semibold disabled:opacity-55 ${className}`} disabled={disabled} onClick={onClick} type="button">
      {label}
    </button>
  );
}
