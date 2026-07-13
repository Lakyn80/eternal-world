import { Suspense } from "react";

import FamilyMemoryReviewPage from "../../components/family-memory-review-page";

export default function FamilyMemoryReviewRoute() {
  return (
    <Suspense fallback={null}>
      <FamilyMemoryReviewPage />
    </Suspense>
  );
}
