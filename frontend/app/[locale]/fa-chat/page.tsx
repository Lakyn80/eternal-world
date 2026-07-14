import { notFound } from "next/navigation";

import FaChatDemoPage from "../../../components/fa-chat-demo-page";
import { parseAppLocale } from "../../../lib/i18n/locales";

export default function FamilyAvatarChatPage({ params }: { params: { locale: string } }) {
  const locale = parseAppLocale(params.locale);
  if (locale === null) {
    notFound();
  }
  return <FaChatDemoPage locale={locale} />;
}
