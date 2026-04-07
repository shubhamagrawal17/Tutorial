import { test, expect } from '@playwright/test';

test('login and logout flow', async ({ page }) => {
  await page.goto('https://checklyapp.azurewebsites.net');

  // Login
  await page.fill('input[name="username"]', 'admin');
  await page.fill('input[name="password"]', 'password');
  await page.click('button[type="submit"]');

  // Verify login
  await expect(page.locator('h1')).toContainText('Welcome admin');

  // Logout
  await page.click('text=Logout');

  // Verify logout
  await expect(page).toHaveURL(/login/);
});
