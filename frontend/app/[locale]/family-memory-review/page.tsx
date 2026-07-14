import { Suspense } from "react";
import { notFound } from "next/navigation";

import FamilyMemoryReviewPage from "../../../components/family-memory-review-page";
import { parseAppLocale } from "../../../lib/i18n/locales";

export default function FamilyMemoryReviewRoute({ params }: { params: { locale: string } }) {
  const locale = parseAppLocale(params.locale);
  if (locale === null) {
    notFound();
  }
  return (
    <Suspense fallback={null}>
      <FamilyMemoryReviewPage locale={locale} />
    </Suspense>
  );
}
