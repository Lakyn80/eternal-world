import { describe, expect, it } from "vitest";

import { getV2ExperienceContent, getV2Route } from "../lib/v2-experience/content";

describe("v2 experience content", () => {
  it("builds localized preview routes", () => {
    expect(getV2Route("cs")).toBe("/cs/v2");
    expect(getV2Route("ru")).toBe("/ru/v2");
    expect(getV2Route("en")).toBe("/en/v2");
  });

  it("exposes complete core content for every locale", () => {
    for (const locale of ["cs", "ru", "en"] as const) {
      const content = getV2ExperienceContent(locale);

      expect(content.navigation.links.length).toBeGreaterThanOrEqual(5);
      expect(content.hero.workspaceLinks.length).toBe(3);
      expect(content.conversation.suggestions.length).toBe(3);
      expect(content.features.items.length).toBeGreaterThanOrEqual(6);
      expect(content.timeline.items.length).toBeGreaterThanOrEqual(5);
      expect(content.moments.items.length).toBe(3);
    }
  });
});
