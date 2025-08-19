const puppeteer = require('puppeteer');
const fs = require('fs');

async function openLoginPage() {
    const browser = await puppeteer.launch({ headless: false });
    const page = await browser.newPage();
  
    // Navigate to URL
    const url = 'https://ohiostategolfclub.clubhouseonline-e3.com/';
    await page.goto(url);
  
    // Click on Login tab
    await page.waitForSelector('#p_lt_banner_right_SignOutButton_btnSignOutLink');
    await page.click('#p_lt_banner_right_SignOutButton_btnSignOutLink');
  
    // Fill in the login form
    await page.waitForSelector('#p_lt_content_pageplaceholder_p_lt_zoneLeft_CHOLogin_LoginControl_ctl00_Login1_UserName');
    await page.type('#p_lt_content_pageplaceholder_p_lt_zoneLeft_CHOLogin_LoginControl_ctl00_Login1_UserName', 'MMiller');
    await page.type('#p_lt_content_pageplaceholder_p_lt_zoneLeft_CHOLogin_LoginControl_ctl00_Login1_Password', 'Cp6$nb%*');
  
    // Click login
    await page.click('#p_lt_content_pageplaceholder_p_lt_zoneLeft_CHOLogin_LoginControl_ctl00_Login1_LoginButton');

    // Wait for navigation or a selector that confirms login success
    await page.waitForNavigation({ waitUntil: 'networkidle0' });

    // Get cookies
    const cookies = await page.cookies();

    // Save cookies to a file
    fs.writeFileSync('cookies.json', JSON.stringify(cookies, null, 2));

    console.log('Cookies saved to cookies.json');

    // Optionally close browser
    await browser.close();
}
