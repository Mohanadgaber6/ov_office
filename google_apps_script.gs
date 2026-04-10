// ====================================================
// Google Apps Script — أوفي للخدمات الإلكترونية
// ====================================================
// تعليمات النشر:
// 1. افتح Google Sheets جديد وسمّه "طلبات أوفي"
// 2. من القائمة: Extensions → Apps Script
// 3. احذف الكود الموجود والصق هذا الكود كاملاً
// 4. احفظ (Ctrl+S)
// 5. اضغط Deploy → New Deployment
// 6. اختر Type: Web App
// 7. Execute as: Me | Who has access: Anyone
// 8. اضغط Deploy وانسخ الـ URL
// 9. ضع الـ URL في script.js في متغير GOOGLE_SHEET_URL
// ====================================================

function doPost(e) {
  try {
    const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
    
    // إضافة عناوين الأعمدة إذا كانت الورقة فارغة
    if (sheet.getLastRow() === 0) {
      sheet.appendRow([
        'الاسم الكامل',
        'رقم الهاتف / واتساب',
        'البريد الإلكتروني',
        'الخدمة المطلوبة',
        'الرسالة',
        'تاريخ التسجيل',
        'وقت التسجيل'
      ]);
      // تنسيق صف العناوين
      const headerRange = sheet.getRange(1, 1, 1, 7);
      headerRange.setBackground('#293287');
      headerRange.setFontColor('#ffffff');
      headerRange.setFontWeight('bold');
      headerRange.setHorizontalAlignment('center');
    }
    
    const data = JSON.parse(e.postData.contents);
    
    // إضافة صف جديد بالبيانات
    sheet.appendRow([
      data.name    || '—',
      data.phone   || '—',
      data.email   || '—',
      data.service || '—',
      data.message || '—',
      data.date    || new Date().toLocaleDateString('ar-SA'),
      data.time    || new Date().toLocaleTimeString('ar-SA'),
    ]);
    
    // تنسيق تلقائي للأعمدة
    sheet.autoResizeColumns(1, 7);
    
    return ContentService
      .createTextOutput(JSON.stringify({ status: 'success', message: 'تم الحفظ بنجاح' }))
      .setMimeType(ContentService.MimeType.JSON);
      
  } catch (err) {
    return ContentService
      .createTextOutput(JSON.stringify({ status: 'error', message: err.toString() }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}

// للاختبار من المتصفح
function doGet(e) {
  return ContentService
    .createTextOutput(JSON.stringify({ status: 'ok', message: 'أوفي Script يعمل بشكل صحيح' }))
    .setMimeType(ContentService.MimeType.JSON);
}
