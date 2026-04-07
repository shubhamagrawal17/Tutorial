import { test, expect } from '@playwright/test';

test('login and logout flow', async ({ page }) => {
  await page.goto('http://localhost:3000');

  await page.fill('input[name="username"]', 'admin');
  await page.fill('input[name="password"]', 'password');
  await page.click('button[type="submit"]');

  await expect(page.locator('h1')).toContainText('Welcome admin');

  await page.click('text=Logout');

  await expect(page).toHaveURL(/login/);
});
