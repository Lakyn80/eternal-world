import { expect, test, type Page } from "@playwright/test";

const locales = ["cs", "ru", "en"] as const;

const routeSuffixes = ["", "/v2", "/fa-chat", "/family-memory-review", "/presentation"] as const;

const viewports = [
  { name: "mobile-320", width: 320, height: 568 },
  { name: "mobile-375", width: 375, height: 667 },
  { name: "mobile-390", width: 390, height: 844 },
  { name: "mobile-414", width: 414, height: 896 },
  { name: "tablet-768", width: 768, height: 1024 },
  { name: "tablet-landscape-1024", width: 1024, height: 768 },
  { name: "desktop-1280", width: 1280, height: 720 },
  { name: "desktop-1440", width: 1440, height: 900 },
  { name: "desktop-1920", width: 1920, height: 1080 },
] as const;

type OverflowIssue = {
  selector: string;
  left: number;
  right: number;
  width: number;
  viewportWidth: number;
  text: string;
};

async function waitForPageToSettle(page: Page) {
  await page.waitForLoadState("domcontentloaded");
  await page.locator("body").waitFor({ state: "visible" });
  await page.waitForTimeout(250);
}

async function getHorizontalOverflow(page: Page) {
  return page.evaluate(() => {
    const documentWidth = document.documentElement.clientWidth;
    const rootScrollWidth = Math.ceil(document.documentElement.scrollWidth);
    const bodyScrollWidth = Math.ceil(document.body.scrollWidth);

    return {
      documentWidth,
      scrollWidth: Math.max(rootScrollWidth, bodyScrollWidth),
    };
  });
}

async function findViewportIssues(page: Page): Promise<OverflowIssue[]> {
  return page.evaluate(() => {
    const viewportWidth = document.documentElement.clientWidth;
    const selectors = [
      "main",
      "nav",
      "section",
      "a",
      "button",
      "input",
      "textarea",
      "select",
      "[role='button']",
      "[role='region']",
      "[class*='page']",
      "[class*='layout']",
      "[class*='workspace']",
      "[class*='hero']",
      "[class*='deck']",
      "[class*='card']",
      "[class*='panel']",
    ].join(",");

    function selectorFor(element: Element) {
      if (element.id) {
        return `#${element.id}`;
      }
      const className =
        typeof (element as HTMLElement).className === "string"
          ? (element as HTMLElement).className.trim().split(/\s+/).slice(0, 3).join(".")
          : "";
      return `${element.tagName.toLowerCase()}${className ? `.${className}` : ""}`;
    }

    return Array.from(document.querySelectorAll<HTMLElement>(selectors))
      .filter((element) => {
        const style = window.getComputedStyle(element);
        if (style.display === "none" || style.visibility === "hidden" || element.hidden) {
          return false;
        }
        if (element.closest("[aria-hidden='true']")) {
          return false;
        }
        return true;
      })
      .map((element) => {
        const rect = element.getBoundingClientRect();
        return {
          selector: selectorFor(element),
          left: Math.floor(rect.left),
          right: Math.ceil(rect.right),
          width: Math.ceil(rect.width),
          viewportWidth,
          text: (element.innerText || element.getAttribute("aria-label") || "").trim().slice(0, 90),
        };
      })
      .filter((issue) => issue.width > 0 && (issue.left < -1 || issue.right > issue.viewportWidth + 1))
      .slice(0, 20);
  });
}

for (const locale of locales) {
  for (const suffix of routeSuffixes) {
    test(`${locale}${suffix || "/"} has no horizontal overflow`, async ({ page }) => {
      const route = `/${locale}${suffix}`;

      for (const viewport of viewports) {
        await page.setViewportSize({ width: viewport.width, height: viewport.height });

        await page.goto(route, { waitUntil: "domcontentloaded" });
        await waitForPageToSettle(page);

        const overflow = await getHorizontalOverflow(page);
        expect(overflow.scrollWidth, `${route} scrollWidth at ${viewport.name}`).toBeLessThanOrEqual(
          overflow.documentWidth + 1
        );

        const issues = await findViewportIssues(page);
        expect(issues, `${route} off-viewport elements at ${viewport.name}`).toEqual([]);
      }
    });
  }
}
