import re
import os

path = r'c:\Users\ADMIN\OneDrive\Desktop\اوفي\index.html'
with open(path, 'r', encoding='utf-8') as f:
    html_content = f.read()

base_items = """
            <li class="pkg-accordion-item">
              <div class="pkg-accordion-header">
                <span class="pkg-feat-title">✅ إدارة خدمات وزارة العمل</span>
                <span class="pkg-expand-icon">
                  <svg viewBox="0 0 24 24" width="20" height="20" stroke="currentColor" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14M5 12h14"/></svg>
                </span>
              </div>
              <ul class="pkg-accordion-body">
                <li>تسجيل بمنصة قوى</li>
                <li>رخص العمل</li>
                <li>إدارة المهن</li>
                <li>إصدار شهادة السعودة</li>
                <li>تأشيرات العمل الفوري</li>
                <li>نقل الخدمات</li>
                <li>تجديد اشتراك بمنصة قوى</li>
              </ul>
            </li>
            <li class="pkg-accordion-item">
              <div class="pkg-accordion-header">
                <span class="pkg-feat-title">✅ إدارة خدمات التأمينات الاجتماعية</span>
                <span class="pkg-expand-icon">
                  <svg viewBox="0 0 24 24" width="20" height="20" stroke="currentColor" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14M5 12h14"/></svg>
                </span>
              </div>
              <ul class="pkg-accordion-body">
                <li>استكمال بيانات المنشأة</li>
                <li>إضافة مدير حساب الفروع</li>
                <li>تسجيل موظفين</li>
                <li>تحديث أجور</li>
                <li>إصدار شهادة التزام التأمينات</li>
              </ul>
            </li>
            <li class="pkg-accordion-item">
              <div class="pkg-accordion-header">
                <span class="pkg-feat-title">✅ إدارة خدمات وزارة التجارة</span>
                <span class="pkg-expand-icon">
                  <svg viewBox="0 0 24 24" width="20" height="20" stroke="currentColor" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14M5 12h14"/></svg>
                </span>
              </div>
              <ul class="pkg-accordion-body">
                <li>اصدار سجل تجاري</li>
                <li>تجديد سجل تجاري</li>
                <li>تعديل سجل تجاري</li>
              </ul>
            </li>
            <li class="pkg-accordion-item">
              <div class="pkg-accordion-header">
                <span class="pkg-feat-title">✅ إدارة خدمات الهيئة العامة للزكاة</span>
                <span class="pkg-expand-icon">
                  <svg viewBox="0 0 24 24" width="20" height="20" stroke="currentColor" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14M5 12h14"/></svg>
                </span>
              </div>
              <ul class="pkg-accordion-body">
                <li>التسجيل في ضريبة القيمة المضافة</li>
                <li>رفع الإقرارات الضريبية</li>
                <li>تحديث بيانات الرقم المميز</li>
                <li>التسجل في الزكاة والدخل</li>
              </ul>
            </li>
            <li class="pkg-accordion-item">
              <div class="pkg-accordion-header">
                <span class="pkg-feat-title">✅ إدارة خدمات وزارة الداخلية</span>
                <span class="pkg-expand-icon">
                  <svg viewBox="0 0 24 24" width="20" height="20" stroke="currentColor" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14M5 12h14"/></svg>
                </span>
              </div>
              <ul class="pkg-accordion-body">
                <li>إصدار وتجديد اقامات</li>
                <li>تأشيرة خروج وعودة / نهائي</li>
                <li>خدمة توصيل الوثائق</li>
                <li>تجديد اشتراك أبشر اعمال</li>
              </ul>
            </li>
            <li class="pkg-accordion-item">
              <div class="pkg-accordion-header">
                <span class="pkg-feat-title">✅ إدارة خدمات بلدي</span>
                <span class="pkg-expand-icon">
                  <svg viewBox="0 0 24 24" width="20" height="20" stroke="currentColor" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14M5 12h14"/></svg>
                </span>
              </div>
              <ul class="pkg-accordion-body">
                <li>إصدار وتجديد رخصة تجارية</li>
                <li>تعديل رخصة تجارية</li>
              </ul>
            </li>
            <li class="pkg-accordion-item">
              <div class="pkg-accordion-header">
                <span class="pkg-feat-title">✅ إدارة خدمات سلامة</span>
                <span class="pkg-expand-icon">
                  <svg viewBox="0 0 24 24" width="20" height="20" stroke="currentColor" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14M5 12h14"/></svg>
                </span>
              </div>
              <ul class="pkg-accordion-body">
                <li>إصدار وتجديد رخصة سلامة</li>
              </ul>
            </li>
            <li class="pkg-accordion-item">
              <div class="pkg-accordion-header">
                <span class="pkg-feat-title">✅ إدارة خدمات شركات التأمين الطبي</span>
                <span class="pkg-expand-icon">
                  <svg viewBox="0 0 24 24" width="20" height="20" stroke="currentColor" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14M5 12h14"/></svg>
                </span>
              </div>
              <ul class="pkg-accordion-body">
                <li>المقارنة بين عروض الاسعار</li>
                <li>ارسال شبكة مزودي الخدمة</li>
              </ul>
            </li>
            <li class="pkg-accordion-item">
              <div class="pkg-accordion-header">
                <span class="pkg-feat-title">✅ خدمات الاستشارات</span>
                <span class="pkg-expand-icon">
                  <svg viewBox="0 0 24 24" width="20" height="20" stroke="currentColor" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14M5 12h14"/></svg>
                </span>
              </div>
              <ul class="pkg-accordion-body">
                <li>تقديم الاستشارات في جميع الخدمات</li>
              </ul>
            </li>
"""

extra_items = """
            <li class="pkg-accordion-item pkg-extra">
              <div class="pkg-accordion-header">
                <span class="pkg-feat-title">✅ اشتراك برنامج حماية الأجور</span>
                <span class="pkg-expand-icon">
                  <svg viewBox="0 0 24 24" width="20" height="20" stroke="currentColor" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14M5 12h14"/></svg>
                </span>
              </div>
              <ul class="pkg-accordion-body">
                <li>التسجيل بمنصة مدد</li>
                <li>رفع الرواتب بشكل شهري</li>
                <li>تحديث بيانات الموظفين</li>
                <li>إزالة ملاحظة حماية الأجور</li>
              </ul>
            </li>
            <li class="pkg-accordion-item pkg-extra">
              <div class="pkg-accordion-header">
                <span class="pkg-feat-title">✅ توثيق عقود العمل للموظفين</span>
                <span class="pkg-expand-icon">
                  <svg viewBox="0 0 24 24" width="20" height="20" stroke="currentColor" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14M5 12h14"/></svg>
                </span>
              </div>
              <ul class="pkg-accordion-body">
                <li>إدارة وتوثيق العقود عبر قوى</li>
              </ul>
            </li>
"""

plat_items = """
            <li class="pkg-accordion-item pkg-plat">
              <div class="pkg-accordion-header">
                <span class="pkg-feat-title">✅ إعداد اللائحة الداخلية للمنشأة</span>
                <span class="pkg-expand-icon">
                  <svg viewBox="0 0 24 24" width="20" height="20" stroke="currentColor" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14M5 12h14"/></svg>
                </span>
              </div>
              <ul class="pkg-accordion-body">
                <li>اعتماد لائحة تنظيم العمل</li>
              </ul>
            </li>
            <li class="pkg-accordion-item pkg-plat">
              <div class="pkg-accordion-header">
                <span class="pkg-feat-title">✅ إعداد عقود العمل لجميع الموظفين</span>
                <span class="pkg-expand-icon">
                  <svg viewBox="0 0 24 24" width="20" height="20" stroke="currentColor" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14M5 12h14"/></svg>
                </span>
              </div>
              <ul class="pkg-accordion-body">
                <li>صياغة العقود نظامياً</li>
              </ul>
            </li>
            <li class="pkg-accordion-item pkg-plat">
              <div class="pkg-accordion-header">
                <span class="pkg-feat-title">✅ تخفيف الأعباء المالية للمنشآت</span>
                <span class="pkg-expand-icon">
                  <svg viewBox="0 0 24 24" width="20" height="20" stroke="currentColor" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14M5 12h14"/></svg>
                </span>
              </div>
              <ul class="pkg-accordion-body">
                <li>التسجيل بمنصة طاقات لدعم التوطين</li>
              </ul>
            </li>
            <li class="pkg-accordion-item pkg-plat">
              <div class="pkg-accordion-header">
                <span class="pkg-feat-title">✅ تأهيل وتدريب موظفين المنشأة</span>
                <span class="pkg-expand-icon">
                  <svg viewBox="0 0 24 24" width="20" height="20" stroke="currentColor" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14M5 12h14"/></svg>
                </span>
              </div>
              <ul class="pkg-accordion-body">
                <li>عمل برامج تأهيلية مستمرة</li>
              </ul>
            </li>
"""

silver_ul = f'<ul class="pkg-features pkg-accordion">\\n{base_items}          </ul>'
gold_ul = f'<ul class="pkg-features pkg-accordion">\\n{base_items}{extra_items}          </ul>'
plat_ul = f'<ul class="pkg-features pkg-accordion">\\n{base_items}{extra_items}{plat_items}          </ul>'

old_silver_pattern = r'<ul class="pkg-features">\s*<li>✅ إدارة خدمات وزارة العمل</li>.*?</<ul>'
html_content = re.sub(r'<ul class="pkg-features">\s*<li>✅ إدارة خدمات وزارة العمل</li>.*?<li>✅ خدمات الاستشارات</li>\s*</ul>', silver_ul, html_content, flags=re.DOTALL)
html_content = re.sub(r'<ul class="pkg-features">\s*<li>✅ إدارة خدمات وزارة العمل</li>.*?<li class="pkg-extra">✅ توثيق عقود العمل للموظفين</li>\s*</ul>', gold_ul, html_content, flags=re.DOTALL)
html_content = re.sub(r'<ul class="pkg-features">\s*<li>✅ إدارة خدمات وزارة العمل</li>.*?<li class="pkg-plat">✅ تأهيل وتدريب موظفين المنشأة</li>\s*</ul>', plat_ul, html_content, flags=re.DOTALL)

with open(path, 'w', encoding='utf-8') as f:
    f.write(html_content)
