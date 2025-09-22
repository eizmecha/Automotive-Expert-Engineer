import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from PIL import Image, ImageTk
from datetime import datetime

class CarExpertSystem:
        
    def __init__(self):
        # قاعدة المعرفة الشاملة (Comprehensive Knowledge Base) - متعددة اللغات
        self.knowledge_base = {
            "ar": {
                # 1. نظام الطاقة والمحرك
                "نظام_الطاقة": {
                    "مشاكل البطارية": {
                        "question": "هل تواجه مشكلة في تشغيل السيارة أو إضاءة المصابيح؟",
                        "why_reason": "للتحقق من مشاكل البطارية التي قد تمنع التشغيل أو تضعف الإضاءة",
                        "symptoms": ["عدم التشغيل", "إضاءة ضعيفة", "لمبة تحذير البطارية"],
                        "diagnosis_steps": [
                            "فحص توصيلات البطارية والتأكد من نظافتها",
                            "قياس جهد البطارية (يجب أن يكون 12.4 فولت على الأقل)",
                            "فحص التيار أثناء التشغيل"
                        ],
                        "solutions": ["شحن البطارية", "تنظيف التوصيلات", "استبدال البطارية"],
                        "recommendation": "استبدل البطارية كل 4-5 سنوات وافحصها دورياً",
                        "emergency": False,
                        "risk_level": "متوسط",
                        "dependencies": {
                            "if_yes": ["مشاكل المولد (الدينمو)", "مشاكل نظام التبريد"],
                            "if_no": ["مشاكل المحرك", "مشاكل مضخة الوقود"]
                        }
                    },
                    
                    "مشاكل المحرك": {
                        "question": "هل تسمع أصوات غير طبيعية من المحرك أو توجد اهتزازات؟",
                        "why_reason": "الأصوات والاهتزازات غير الطبيعية قد تشير إلى مشاكل في المحرك",
                        "symptoms": ["أصوات طرق", "اهتزازات", "لمبة تحذير المحرك", "ضعف الأداء"],
                        "diagnosis_steps": [
                            "فحص مستوى زيت المحرك وجودته",
                            "فحص شمعات الإشعال وأسلاك البواجي",
                            "فحص فلتر الهواء والوقود"
                        ],
                        "solutions": ["تغيير الزيت", "استبدال شمعات الإشعال", "تنظيف فلتر الهواء"],
                        "recommendation": "التزم بمواعيد الصيانة الدورية للمحرك",
                        "emergency": True,
                        "risk_level": "عالي",
                        "dependencies": {
                            "if_yes": ["مشاكل نظام التبريد", "مشاكل ناقل الحركة (القير)"],
                            "if_no": ["مشاكل المولد (الدينمو)", "مشاكل نظام التعليق"]
                        }
                    },
                    
                    "مشاكل المولد (الدينمو)": {
                        "question": "هل تظهر إشارة بطارية على لوحة القيادة أو الأضواء خافتة؟",
                        "why_reason": "المولد مسؤول عن شحن البطارية وتشغيل الأنظمة الكهربائية",
                        "symptoms": ["لمبة تحذير البطارية", "أضواء خافتة", "ضعف في الأنظمة الكهربائية"],
                        "diagnosis_steps": [
                            "فحص جهد المولد أثناء التشغيل",
                            "قياس تيار الشحن",
                            "فحص حزام المولد وتوصيلاته"
                        ],
                        "solutions": ["استبدال المولد", "شد حزام المولد", "إصلاح التوصيلات"],
                        "recommendation": "افحص نظام الشحن دورياً وتأكد من سلامة الحزام",
                        "emergency": True,
                        "risk_level": "عالي",
                        "dependencies": {
                            "if_yes": ["مشاكل البطارية", "مشاكل المصابيح والإضاءة"],
                            "if_no": ["مشاكل نظام التبريد", "مشاكل شمعات الإشعال"]
                        }
                    },
                    
                    "مشاكل مضخة الوقود": {
                        "question": "هل تواجه صعوبة في بدء التشغيل أو توقف المحرك أثناء القيادة؟",
                        "why_reason": "مضخة الوقود مسؤولة عن ضخ الوقود من الخزان إلى المحرك",
                        "symptoms": ["صعوبة التشغيل", "توقف المحرك", "ضعف التسارع", "أصوات طنين"],
                        "diagnosis_steps": [
                            "فحص ضغط الوقود",
                            "الاستماع إلى صوت مضخة الوقود عند تشغيل المفتاح",
                            "فحص التيار الكهربائي للمضخة"
                        ],
                        "solutions": ["استبدال مضخة الوقود", "تنظيف شبكة المضخة", "فحص التوصيلات"],
                        "recommendation": "استبدل فلتر الوقود بانتظام لحماية المضخة",
                        "emergency": True,
                        "risk_level": "عالي",
                        "dependencies": {
                            "if_yes": ["مشاكل فلتر الوقود", "مشاكل حاقنات الوقود"],
                            "if_no": ["مشاكل البطارية", "مشاكل نظام التبريد"]
                        }
                    }
                },
                
                # 2. النظام الكهربائي
                "النظام_الكهربائي": {
                    "مشاكل المصابيح والإضاءة": {
                        "question": "هل هناك مصابيح لا تعمل أو تعمل بشكل غير طبيعي؟",
                        "why_reason": "مشاكل الإضاءة تؤثر على الرؤية والأمان أثناء القيادة",
                        "symptoms": ["مصابيح لا تعمل", "إضاءة خافتة", "وميض غير طبيعي"],
                        "diagnosis_steps": [
                            "فحص المصابيح والتأكد من عدم احتراقها",
                            "فحص الفيوزات الكهربائية",
                            "فحص التوصيلات والأسلاك"
                        ],
                        "solutions": ["استبدال المصابيح", "استبدال الفيوزات", "إصلاح التوصيلات"],
                        "recommendation": "افحص المصابيح دورياً وحافظ على نظافتها",
                        "emergency": False,
                        "risk_level": "منخفض",
                        "dependencies": {
                            "if_yes": ["مشاكل جهاز الإنذار", "مشاكل المولد (الدينمو)"],
                            "if_no": ["مشاكل شمعات الإشعال", "مشاكل نظام التبريد"]
                        }
                    },
                    
                    "مشاكل جهاز الإنذار": {
                        "question": "هل جهاز الإنذار يعمل بشكل غير طبيعي أو دون سبب واضح؟",
                        "why_reason": "أعطال الإنذار قد تسبب إزعاجاً أو تضعف نظام الحماية",
                        "symptoms": ["إنذار يعمل دون سبب", "عدم استجابة للتحكم", "صوت إنذار ضعيف"],
                        "diagnosis_steps": [
                            "فحص بطارية جهاز التحكم",
                            "فحص حساسات الحركة والتصادم",
                            "إعادة برمجة النظام"
                        ],
                        "solutions": ["استبدال بطارية التحكم", "ضبط الحساسات", "إعادة البرمجة"],
                        "recommendation": "حافظ على نظافة الحساسات وافحصها دورياً",
                        "emergency": False,
                        "risk_level": "منخفض",
                        "dependencies": {
                            "if_yes": ["مشاكل البطارية", "مشاكل المصابيح والإضاءة"],
                            "if_no": ["مشاكل الوسائد الهوائية", "مشاكل أحزمة الأمان"]
                        }
                    },
                    
                    "مشاكل شمعات الإشعال": {
                        "question": "هل المحرك يعمل بشكل غير منتظم أو يوجد ضعف في الأداء؟",
                        "why_reason": "شمعات الإشعال التالفة تؤثر على كفاءة الاحتراق في المحرك",
                        "symptoms": ["ضعف التسارع", "اهتزاز المحرك", "استهلاك وقود زائد"],
                        "diagnosis_steps": [
                            "فحص شمعات الإشعال وتنظيفها",
                            "قياس الفجوة بين الأقطاب",
                            "فحص أسلاك البواجي"
                        ],
                        "solutions": ["تنظيف الشمعات", "ضبط الفجوة", "استبدال الشمعات"],
                        "recommendation": "استبدل شمعات الإشعال حسب توصيات الشركة المصنعة",
                        "emergency": False,
                        "risk_level": "متوسط",
                        "dependencies": {
                            "if_yes": ["مشاكل المحرك", "مشاكل حاقنات الوقود"],
                            "if_no": ["مشاكل نظام التبريد", "مشاكل ناقل الحركة (القير)"]
                        }
                    }
                },
                
                # 3. نظام التبريد
                "نظام_التبريد": {
                    "مشاكل نظام التبريد": {
                        "question": "هل ترتفع حرارة المحرك بشكل غير طبيعي؟",
                        "why_reason": "ارتفاع الحرارة قد يتسبب في تلف شديد للمحرك",
                        "symptoms": ["ارتفاع حرارة المحرك", "تسرب سائل التبريد", "رائحة احتراق"],
                        "diagnosis_steps": [
                            "فحص مستوى سائل التبريد",
                            "التأكد من عدم وجود تسريبات",
                            "فحص عمل المروحة والثرموستات"
                        ],
                        "solutions": ["إضافة سائل التبريد", "إصلاح التسريبات", "استبدال المروحة"],
                        "recommendation": "افحص مستوى سائل التبريد أسبوعياً",
                        "emergency": True,
                        "risk_level": "عالي",
                        "dependencies": {
                            "if_yes": ["تسرب المبرد (الرادياتير)", "مشاكل المحرك"],
                            "if_no": ["مشاكل البطارية", "مشاكل المولد (الدينمو)"]
                        }
                    },
                    
                    "تسرب المبرد (الرادياتير)": {
                        "question": "هل توجد بقع خضراء أو صفراء تحت السيارة؟",
                        "why_reason": "تسرب سائل التبريد يؤدي إلى ارتفاع حرارة المحرك",
                        "symptoms": ["بقع سائل تحت السيارة", "انخفاض مستوى التبريد", "رائحة حلوة"],
                        "diagnosis_steps": [
                            "فحص الرادياتير للتأكد من عدم وجود تسريبات",
                            "فحص الأنابيب والوصلات",
                            "فحص غطاء الرادياتير"
                        ],
                        "solutions": ["إصلاح التسريبات", "استبدال الرادياتير", "تغيير الأنابيب"],
                        "recommendation": "افحص نظام التبريد قبل الرحلات الطويلة",
                        "emergency": True,
                        "risk_level": "عالي",
                        "dependencies": {
                            "if_yes": ["مشاكل نظام التبريد", "مشاكل المحرك"],
                            "if_no": ["مشاكل تدفئة السيارة", "مشاكل نظام التبريد"]
                        }
                    }
                },
                
                # 4. نظام نقل الحركة
                "نقل_الحركة": {
                    "مشاكل ناقل الحركة (القير)": {
                        "question": "هل تواجه صعوبة في تغيير السرعات أو تسمع أصواتاً من القير؟",
                        "why_reason": "مشاكل ناقل الحركة تؤثر على أداء السيارة وسلامة القيادة",
                        "symptoms": ["صعوبة تغيير السرعات", "أصوات طنين", "اهتزازات"],
                        "diagnosis_steps": [
                            "فحص مستوى زيت ناقل الحركة",
                            "فحص جودة الزيت ولونه",
                            "فحص الوصلات والتوصيلات"
                        ],
                        "solutions": ["تغيير زيت الناقل", "ضبط الوصلات", "صيانة شاملة"],
                        "recommendation": "غير زيت ناقل الحركة حسب توصيات الشركة الصانعة",
                        "emergency": False,
                        "risk_level": "متوسط",
                        "dependencies": {
                            "if_yes": ["مشاكل الدبرياج (القابض)", "مشاكل المحرك"],
                            "if_no": ["مشاكل نظام التعليق", "مشاكل نظام الفرامل"]
                        }
                    },
                    
                    "مشاكل الدبرياج (القابض)": {
                        "question": "هل تسمع صوت صرير عند الضغط على دواسة الدبرياج؟",
                        "why_reason": "مشاكل الدبرياج تؤثر على نقل الحركة من المحرك إلى العجلات",
                        "symptoms": ["صرير عند الضغط", "انزلاق الدبرياج", "رائحة احتراق"],
                        "diagnosis_steps": [
                            "فحص مستوى زيت الدبرياج",
                            "فحص سماكة طبقتي الدبرياج",
                            "فحص نظام الهيدروليك"
                        ],
                        "solutions": ["ضبط الدبرياج", "استبدال طبقتي الدبرياج", "تغيير الزيت"],
                        "recommendation": "لا تترك قدمك على دواسة الدبرياج أثناء القيادة",
                        "emergency": False,
                        "risk_level": "متوسط",
                        "dependencies": {
                            "if_yes": ["مشاكل ناقل الحركة (القير)", "مشاكل نظام الفرامل"],
                            "if_no": ["مشاكل نظام التوجيه", "مشاكل نظام التعليق"]
                        }
                    }
                },
                
                # 5. نظام التوجيه والتعليق
                "التوجيه_والتعليق": {
                    "مشاكل نظام التوجيه": {
                        "question": "هل تواجه صعوبة في توجيه المقود أو تسمع أصواتاً منه؟",
                        "why_reason": "مشاكل التوجيه قد تؤثر على التحكم في السيارة وسلامة القيادة",
                        "symptoms": ["صعوبة التوجيه", "أصوات طقطقة", "انحراف السيارة"],
                        "diagnosis_steps": [
                            "فحص مستوى زيت التوجيه",
                            "فحص المساعدات والوصلات",
                            "فحص توازن العجلات"
                        ],
                        "solutions": ["إضافة زيت التوجيه", "استبدال المساعدات", "عمل توازن"],
                        "recommendation": "افحص نظام التوجيه دورياً وحافظ على نظافة الزيت",
                        "emergency": True,
                        "risk_level": "عالي",
                        "dependencies": {
                            "if_yes": ["مشاكل نظام التعليق", "مشاكل توازن العجلات"],
                            "if_no": ["مشاكل الدبرياج (القابض)", "مشاكل نظام الفرامل"]
                        }
                    },
                    
                    "مشاكل نظام التعليق": {
                        "question": "هل تسمع أصوات طقطقة عند المرور على المطبات أو المنعطفات؟",
                        "why_reason": "مشاكل التعليق تؤثر على راحة القيادة واستقرار السيارة",
                        "symptoms": ["أصوات طقطقة", "اهتزاز السيارة", "تآكل غير منتظم للإطارات"],
                        "diagnosis_steps": [
                            "فحص المساعدات الأمامية والخلفية",
                            "فحص كراسي الكاوتش",
                            "فحص أذرع التعليق"
                        ],
                        "solutions": ["استبدال المساعدات", "تغيير كراسي الكاوتش", "ضبط التعليق"],
                        "recommendation": "افحص نظام التعليق كل 20,000 كم",
                        "emergency": False,
                        "risk_level": "متوسط",
                        "dependencies": {
                            "if_yes": ["مشاكل توازن العجلات", "مشاكل تسرب الهواء"],
                            "if_no": ["مشاكل نظام التوجيه", "مشاكل نظام الفرامل"]
                        }
                    }
                },
                
                # 6. نظام الفرامل
                "نظام_الفرامل": {
                    "مشاكل وسادات الفرامل": {
                        "question": "هل تسمع صوت صرير عند استخدام الفرامل؟",
                        "why_reason": "الصرير يشير عادة إلى تآكل وسادات الفرامل",
                        "symptoms": ["صرير الفرامل", "ضعف الكبح", "اهتزاز الدواسة"],
                        "diagnosis_steps": [
                            "فحص سمك وسادات الفرامل",
                            "فحص حالة الديسكات أو الطنابير",
                            "فحص مستوى زيت الفرامل"
                        ],
                        "solutions": ["استبدال الوسادات", "تصليح الديسكات", "تغيير زيت الفرامل"],
                        "recommendation": "استبدل وسادات الفرامل عند سماع صوت الصرير المستمر",
                        "emergency": True,
                        "risk_level": "عالي",
                        "dependencies": {
                            "if_yes": ["مشاكل دواسة الفرامل", "مشاكل الدبرياج (القابض)"],
                            "if_no": ["مشاكل نظام التوجيه", "مشاكل نظام التعليق"]
                        }
                    },
                    
                    "مشاكل دواسة الفرامل": {
                        "question": "هل دواسة الفرامل إسفنجية أو تصل إلى الأرض بسهولة؟",
                        "why_reason": "دواسة الفرامل الإسفنجية تشير إلى وجود هواء في النظام",
                        "symptoms": ["دواسة إسفنجية", "مسافة كبح طويلة", "اهتزاز الدواسة"],
                        "diagnosis_steps": [
                            "فحص مستوى زيت الفرامل",
                            "فحص وجود تسريبات في النظام",
                            "تفريغ الهواء من النظام"
                        ],
                        "solutions": ["تفريغ الهواء", "تغيير زيت الفرامل", "إصلاح التسريبات"],
                        "recommendation": "افحص نظام الفرامل كل 10,000 كم",
                        "emergency": True,
                        "risk_level": "عالي",
                        "dependencies": {
                            "if_yes": ["مشاكل وسادات الفرامل", "مشاكل نظام التوجيه"],
                            "if_no": ["مشاكل ناقل الحركة (القير)", "مشاكل نظام التعليق"]
                        }
                    }
                },
                
                # 7. نظام العادم
                "نظام_العادم": {
                    "مشاكل عادم السيارة": {
                        "question": "هل تسمع صوت عادم عالي أو توجد رائحة غازات في السيارة؟",
                        "why_reason": "مشاكل العادم تؤثر على أداء المحرك وتلوث البيئة",
                        "symptoms": ["صوت عادم عالي", "رائحة غازات", "ضعف في الأداء"],
                        "diagnosis_steps": [
                            "فحص كامل نظام العادم للتأكد من عدم وجود تسريبات",
                            "فحص الكاتالايزر",
                            "فحص حساس الأكسجين"
                        ],
                        "solutions": ["إصلاح التسريبات", "استبدال الكاتالايزر", "تنظيف الحساس"],
                        "recommendation": "افحص نظام العادم سنوياً للتأكد من عدم وجود تسريبات",
                        "emergency": False,
                        "risk_level": "متوسط",
                        "dependencies": {
                            "if_yes": ["مشاكل حساس الأكسجين", "مشاكل المحرك"],
                            "if_no": ["مشاكل نظام الوقود", "مشاكل نظام التبريد"]
                        }
                    },
                    
                    "مشاكل حساس الأكسجين": {
                        "question": "هل يوجد استهلاك زائد للوقود أو ضعف في عزم المحرك؟",
                        "why_reason": "حساس الأكسجين يؤثر على خلط الوقود والهواء في المحرك",
                        "symptoms": ["استهلاك وقود زائد", "ضعف العزم", "صعوبة في التشغيل"],
                        "diagnosis_steps": [
                            "قراءة أكواد العطل بجهاز OBD2",
                            "فحص إشارة حساس الأكسجين",
                            "فحص التوصيلات الكهربائية"
                        ],
                        "solutions": ["تنظيف الحساس", "استبدال حساس الأكسجين", "فحص التوصيلات"],
                        "recommendation": "استبدل حساس الأكسجين كل 100,000 كم",
                        "emergency": False,
                        "risk_level": "متوسط",
                        "dependencies": {
                            "if_yes": ["مشاكل عادم السيارة", "مشاكل حاقنات الوقود"],
                            "if_no": ["مشاكل فلتر الوقود", "مشاكل شمعات الإشعال"]
                        }
                    }
                },
                
                # 8. الإطارات والعجلات
                "الإطارات_والعجلات": {
                    "مشاكل تسرب الهواء": {
                        "question": "هل تفقد الإطارات الهواء بسرعة أو تحتاج لتعبئة متكررة؟",
                        "why_reason": "تسرب الهواء يؤثر على كفاءة الوقود وسلامة القيادة",
                        "symptoms": ["فقدان الهواء", "انخفاض الضغط", "تآكل غير منتظم"],
                        "diagnosis_steps": [
                            "فحص ضغط الهواء في جميع الإطارات",
                            "البحث عن ثقوب أو تلف في الإطارات",
                            "فحص الصمامات والحليات"
                        ],
                        "solutions": ["إصلاح الثقوب", "استبدال الصمامات", "استبدال الإطار"],
                        "recommendation": "افحص ضغط الإطارات أسبوعياً وقبل الرحلات الطويلة",
                        "emergency": False,
                        "risk_level": "متوسط",
                        "dependencies": {
                            "if_yes": ["مشاكل توازن العجلات", "مشاكل نظام التعليق"],
                            "if_no": ["مشاكل نظام الفرامل", "مشاكل نظام التوجيه"]
                        }
                    },
                    
                    "مشاكل توازن العجلات": {
                        "question": "هل يوجد اهتزاز في عجلة القيادة عند السرعات العالية؟",
                        "why_reason": "عدم توازن العجلات يسبب اهتزازات ويؤثر على سلامة القيادة",
                        "symptoms": ["اهتزاز عجلة القيادة", "تآكل غير منتظم للإطارات", "أصوات طنين"],
                        "diagnosis_steps": [
                            "فحص توازن العجلات على الجهاز",
                            "فحص استقامة العجلات",
                            "فحص كراسي العجلات"
                        ],
                        "solutions": ["عمل توازن للعجلات", "ضبط استقامة العجلات", "استبدال الكراسي"],
                        "recommendation": "اعمل توازن للعجلات كل 10,000 كم أو عند تبديل الإطارات",
                        "emergency": False,
                        "risk_level": "متوسط",
                        "dependencies": {
                            "if_yes": ["مشاكل تسرب الهواء", "مشاكل نظام التعليق"],
                            "if_no": ["مشاكل نظام التوجيه", "مشاكل نظام الفرامل"]
                        }
                    }
                },
                
                # 9. نظام التكييف والتدفئة
                "التكييف_والتدفئة": {
                    "مشاكل تبريد المكيف": {
                        "question": "هل مكيف الهواء لا يبرد بشكل كافٍ؟",
                        "why_reason": "ضعف التبريد يؤثر على الراحة أثناء القيادة",
                        "symptoms": ["هواء غير بارد", "ضعف التبريد", "روائح كريهة"],
                        "diagnosis_steps": [
                            "فحص فلتر الهواء الداخلي",
                            "فحص شحنة الغاز في النظام",
                            "فحص ضغط الكمبروسر"
                        ],
                        "solutions": ["تنظيف الفلتر", "شحن الغاز", "صيانة الكمبروسر"],
                        "recommendation": "قم بتنظيف فلتر المكيف كل 6 أشهر",
                        "emergency": False,
                        "risk_level": "منخفض",
                        "dependencies": {
                            "if_yes": ["مشاكل تدفئة السيارة", "مشاكل المولد (الدينمو)"],
                            "if_no": ["مشاكل نظام التبريد", "مشاكل البطارية"]
                        }
                    },
                    
                    "مشاكل تدفئة السيارة": {
                        "question": "هل نظام التدفئة لا يعمل بشكل جيد في الأجواء الباردة؟",
                        "why_reason": "نظام التدفئة مهم للراحة أثناء القيادة في الطقس البارد",
                        "symptoms": ["هواء غير ساخن", "ضعف التدفئة", "روائح غريبة"],
                        "diagnosis_steps": [
                            "فحص مستوى سائل التبريد",
                            "فحص صمام التدفئة",
                            "فحص مراوح التدفئة"
                        ],
                        "solutions": ["إضافة سائل التبريد", "استبدال الصمام", "تنظيف المجاري"],
                        "recommendation": "افحص نظام التدفئة قبل فصل الشتاء",
                        "emergency": False,
                        "risk_level": "منخفض",
                        "dependencies": {
                            "if_yes": ["مشاكل تبريد المكيف", "مشاكل نظام التبريد"],
                            "if_no": ["مشاكل البطارية", "مشاكل النظام الكهربائي"]
                        }
                    }
                },
                
                # 10. أنظمة السلامة
                "أنظمة_السلامة": {
                    "مشاكل الوسائد الهوائية": {
                        "question": "هل ضوء تحذير الوسائد الهوائية مضاء في لوحة العدادات؟",
                        "why_reason": "الوسائد الهوائية ضرورية للحماية في حالة الحوادث",
                        "symptoms": ["لمبة تحذير الوسائد", "عدم عمل الوسائد", "أصوات تحذير"],
                        "diagnosis_steps": [
                            "قراءة أكواد العطل بجهاز OBD2",
                            "فحص وحدة التحكم في الوسائد",
                            "فحص التوصيلات والحساسات"
                        ],
                        "solutions": ["إعادة ضبط النظام", "استبدال الحساسات", "صيانة الوحدة"],
                        "recommendation": "لا تقم بإجراء أي إصلاحات للوسائد الهوائية بنفسك",
                        "emergency": True,
                        "risk_level": "عالي",
                        "dependencies": {
                            "if_yes": ["مشاكل أحزمة الأمان", "مشاكل جهاز الإنذار"],
                            "if_no": ["مشاكل النظام الكهربائي", "مشاكل البطارية"]
                        }
                    },
                    
                    "مشاكل أحزمة الأمان": {
                        "question": "هل أحزمة الأمان لا تعمل بشكل صحيح أو تتعطل؟",
                        "why_reason": "أحزمة الأمان هي خط الدفاع الأول في حالة الحوادث",
                        "symptoms": ["أحزمة لا تثبت", "صعوبة في السحب", "أصوات طقطقة"],
                        "diagnosis_steps": [
                            "فحص آلية القفل في الأحزمة",
                            "فحص بكرات الأحزمة",
                            "فحص التوصيلات الكهربائية"
                        ],
                        "solutions": ["تنظيف الآليات", "استبدال الأحزمة", "إصلاح أنظمة القفل"],
                        "recommendation": "افحص أحزمة الأمان دورياً وتأكد من عملها بشكل صحيح",
                        "emergency": True,
                        "risk_level": "عالي",
                        "dependencies": {
                            "if_yes": ["مشاكل الوسائد الهوائية", "مشاكل جهاز الإنذار"],
                            "if_no": ["مشاكل نظام الفرامل", "مشاكل نظام التوجيه"]
                        }
                    }
                },
                
                # 11. نظام الوقود
                "نظام_الوقود": {
                    "مشاكل فلتر الوقود": {
                        "question": "هل يوجد ضعف في عزم المحرك أو توقف مفاجئ أثناء القيادة؟",
                        "why_reason": "فلتر الوقود المسدود يمنع تدفق الوقود إلى المحرك",
                        "symptoms": ["ضعف العزم", "توقف المحرك", "استهلاك وقود زائد"],
                        "diagnosis_steps": [
                            "فحص ضغط الوقود",
                            "فحص فلتر الوقود",
                            "فحص مضخة الوقود"
                        ],
                        "solutions": ["استبدال فلتر الوقود", "تنظيف النظام", "فحص المضخة"],
                        "recommendation": "استبدل فلتر الوقود كل 20,000 كم",
                        "emergency": False,
                        "risk_level": "متوسط",
                        "dependencies": {
                            "if_yes": ["مشاكل حاقنات الوقود", "مشاكل مضخة الوقود"],
                            "if_no": ["مشاكل شمعات الإشعال", "مشاكل المحرك"]
                        }
                    },
                    
                    "مشاكل حاقنات الوقود": {
                        "question": "هل المحرك يعمل بشكل غير منتظم أو يوجد اهتزازات؟",
                        "why_reason": "حاقنات الوقود المسدودة تؤثر على كفاءة الاحتراق",
                        "symptoms": ["اهتزاز المحرك", "ضعف الأداء", "استهلاك وقود زائد"],
                        "diagnosis_steps": [
                            "فحص حاقنات الوقود بالجهاز",
                            "قياس ضغط الحقن",
                            "فحص التوصيلات الكهربائية"
                        ],
                        "solutions": ["تنظيف الحاقنات", "استبدال الحاقنات", "ضبط الضغط"],
                        "recommendation": "استخدم وقود عالي الجودة ونظف الحاقنات دورياً",
                        "emergency": False,
                        "risk_level": "متوسط",
                        "dependencies": {
                            "if_yes": ["مشاكل فلتر الوقود", "مشاكل حساس الأكسجين"],
                            "if_no": ["مشاكل شمعات الإشعال", "مشاكل نظام التبريد"]
                        }
                    }
                }
            },
            
            "en": {
                # 1. Power and Engine System
                "power_system": {
                    "battery_problems": {
                        "question": "Do you have problems starting the car or with lighting?",
                        "why_reason": "To check for battery issues that may prevent starting or weaken lighting",
                        "symptoms": ["Failure to start", "Weak lighting", "Battery warning light"],
                        "diagnosis_steps": [
                            "Check battery connections and ensure they are clean",
                            "Measure battery voltage (should be at least 12.4 volts)",
                            "Check current during operation"
                        ],
                        "solutions": ["Charge battery", "Clean connections", "Replace battery"],
                        "recommendation": "Replace battery every 4-5 years and check regularly",
                        "emergency": False,
                        "risk_level": "medium",
                        "dependencies": {
                            "if_yes": ["alternator_problems", "cooling_system_problems"],
                            "if_no": ["engine_problems", "fuel_pump_problems"]
                        }
                    },
                    
                    "engine_problems": {
                        "question": "Do you hear abnormal sounds from the engine or experience vibrations?",
                        "why_reason": "Abnormal sounds and vibrations may indicate engine problems",
                        "symptoms": ["Knocking sounds", "Vibrations", "Engine warning light", "Poor performance"],
                        "diagnosis_steps": [
                            "Check engine oil level and quality",
                            "Check spark plugs and ignition wires",
                            "Check air and fuel filters"
                        ],
                        "solutions": ["Change oil", "Replace spark plugs", "Clean air filter"],
                        "recommendation": "Follow regular engine maintenance schedule",
                        "emergency": True,
                        "risk_level": "high",
                        "dependencies": {
                            "if_yes": ["cooling_system_problems", "transmission_problems"],
                            "if_no": ["alternator_problems", "suspension_problems"]
                        }
                    },
                    
                    "alternator_problems": {
                        "question": "Is the battery warning light on or are lights dim?",
                        "why_reason": "Alternator is responsible for charging battery and powering electrical systems",
                        "symptoms": ["Battery warning light", "Dim lights", "Weak electrical systems"],
                        "diagnosis_steps": [
                            "Check alternator voltage during operation",
                            "Measure charging current",
                            "Check alternator belt and connections"
                        ],
                        "solutions": ["Replace alternator", "Tighten belt", "Repair connections"],
                        "recommendation": "Regularly check charging system and ensure belt integrity",
                        "emergency": True,
                        "risk_level": "high",
                        "dependencies": {
                            "if_yes": ["battery_problems", "lighting_problems"],
                            "if_no": ["cooling_system_problems", "spark_plug_problems"]
                        }
                    },
                    
                    "fuel_pump_problems": {
                        "question": "Do you have difficulty starting or does engine stop while driving?",
                        "why_reason": "Fuel pump is responsible for pumping fuel from tank to engine",
                        "symptoms": ["Starting difficulty", "Engine stopping", "Poor acceleration", "Whining sounds"],
                        "diagnosis_steps": [
                            "Check fuel pressure",
                            "Listen to fuel pump sound when turning key",
                            "Check electrical current to pump"
                        ],
                        "solutions": ["Replace fuel pump", "Clean pump screen", "Check connections"],
                        "recommendation": "Regularly replace fuel filter to protect pump",
                        "emergency": True,
                        "risk_level": "high",
                        "dependencies": {
                            "if_yes": ["fuel_filter_problems", "fuel_injector_problems"],
                            "if_no": ["battery_problems", "cooling_system_problems"]
                        }
                    }
                },
                
                # 2. Electrical System
                "electrical_system": {
                    "lighting_problems": {
                        "question": "Are there lights that don't work or work abnormally?",
                        "why_reason": "Lighting problems affect visibility and safety while driving",
                        "symptoms": ["Lights not working", "Dim lighting", "Abnormal flickering"],
                        "diagnosis_steps": [
                            "Check lights and ensure they are not burned out",
                            "Check electrical fuses",
                            "Check connections and wiring"
                        ],
                        "solutions": ["Replace lights", "Replace fuses", "Repair connections"],
                        "recommendation": "Regularly check lights and keep them clean",
                        "emergency": False,
                        "risk_level": "low",
                        "dependencies": {
                            "if_yes": ["alarm_system_problems", "alternator_problems"],
                            "if_no": ["spark_plug_problems", "cooling_system_problems"]
                        }
                    },
                    
                    "alarm_system_problems": {
                        "question": "Does the alarm system work abnormally or without clear reason?",
                        "why_reason": "Alarm malfunctions may cause annoyance or weaken protection system",
                        "symptoms": ["Alarm activates without reason", "No response to control", "Weak alarm sound"],
                        "diagnosis_steps": [
                            "Check control unit battery",
                            "Check motion and impact sensors",
                            "Reprogram system"
                        ],
                        "solutions": ["Replace control battery", "Adjust sensors", "Reprogram"],
                        "recommendation": "Keep sensors clean and check them regularly",
                        "emergency": False,
                        "risk_level": "low",
                        "dependencies": {
                            "if_yes": ["battery_problems", "lighting_problems"],
                            "if_no": ["airbag_problems", "seatbelt_problems"]
                        }
                    },
                    
                    "spark_plug_problems": {
                        "question": "Does the engine run irregularly or have poor performance?",
                        "why_reason": "Faulty spark plugs affect combustion efficiency in the engine",
                        "symptoms": ["Poor acceleration", "Engine vibration", "Excessive fuel consumption"],
                        "diagnosis_steps": [
                            "Check and clean spark plugs",
                            "Measure electrode gap",
                            "Check ignition wires"
                        ],
                        "solutions": ["Clean plugs", "Adjust gap", "Replace spark plugs"],
                        "recommendation": "Replace spark plugs according to manufacturer recommendations",
                        "emergency": False,
                        "risk_level": "medium",
                        "dependencies": {
                            "if_yes": ["engine_problems", "fuel_injector_problems"],
                            "if_no": ["cooling_system_problems", "transmission_problems"]
                        }
                    }
                },
                
                # 3. Cooling System
                "cooling_system": {
                    "cooling_system_problems": {
                        "question": "Does engine temperature rise abnormally?",
                        "why_reason": "Overheating can cause severe engine damage",
                        "symptoms": ["Engine overheating", "Coolant leakage", "Burning smell"],
                        "diagnosis_steps": [
                            "Check coolant level",
                            "Ensure no leaks",
                            "Check fan and thermostat operation"
                        ],
                        "solutions": ["Add coolant", "Repair leaks", "Replace fan"],
                        "recommendation": "Check coolant level weekly",
                        "emergency": True,
                        "risk_level": "high",
                        "dependencies": {
                            "if_yes": ["radiator_leak", "engine_problems"],
                            "if_no": ["battery_problems", "alternator_problems"]
                        }
                    },
                    
                    "radiator_leak": {
                        "question": "Are there green or yellow spots under the car?",
                        "why_reason": "Coolant leak leads to engine overheating",
                        "symptoms": ["Fluid spots under car", "Low coolant level", "Sweet smell"],
                        "diagnosis_steps": [
                            "Check radiator for leaks",
                            "Check hoses and connections",
                            "Check radiator cap"
                        ],
                        "solutions": ["Repair leaks", "Replace radiator", "Change hoses"],
                        "recommendation": "Check cooling system before long trips",
                        "emergency": True,
                        "risk_level": "high",
                        "dependencies": {
                            "if_yes": ["cooling_system_problems", "engine_problems"],
                            "if_no": ["heating_problems", "cooling_system_problems"]
                        }
                    }
                },
                
                # 4. Transmission System
                "transmission_system": {
                    "transmission_problems": {
                        "question": "Do you have difficulty changing gears or hear sounds from transmission?",
                        "why_reason": "Transmission problems affect car performance and driving safety",
                        "symptoms": ["Difficulty changing gears", "Whining sounds", "Vibrations"],
                        "diagnosis_steps": [
                            "Check transmission fluid level",
                            "Check fluid quality and color",
                            "Check connections and linkages"
                        ],
                        "solutions": ["Change transmission fluid", "Adjust linkages", "Complete maintenance"],
                        "recommendation": "Change transmission fluid according to manufacturer recommendations",
                        "emergency": False,
                        "risk_level": "medium",
                        "dependencies": {
                            "if_yes": ["clutch_problems", "engine_problems"],
                            "if_no": ["suspension_problems", "brake_pad_problems"]
                        }
                    },
                    
                    "clutch_problems": {
                        "question": "Do you hear squealing when pressing clutch pedal?",
                        "why_reason": "Clutch problems affect power transfer from engine to wheels",
                        "symptoms": ["Squealing when pressing", "Clutch slipping", "Burning smell"],
                        "diagnosis_steps": [
                            "Check clutch fluid level",
                            "Check clutch plate thickness",
                            "Check hydraulic system"
                        ],
                        "solutions": ["Adjust clutch", "Replace clutch plates", "Change fluid"],
                        "recommendation": "Don't rest foot on clutch pedal while driving",
                        "emergency": False,
                        "risk_level": "medium",
                        "dependencies": {
                            "if_yes": ["transmission_problems", "brake_pad_problems"],
                            "if_no": ["steering_problems", "suspension_problems"]
                        }
                    }
                },
                
                # 5. Steering and Suspension
                "steering_suspension": {
                    "steering_problems": {
                        "question": "Do you have difficulty steering or hear sounds from steering wheel?",
                        "why_reason": "Steering problems may affect vehicle control and driving safety",
                        "symptoms": ["Steering difficulty", "Clicking sounds", "Vehicle pulling"],
                        "diagnosis_steps": [
                            "Check power steering fluid level",
                            "Check tie rods and connections",
                            "Check wheel alignment"
                        ],
                        "solutions": ["Add power steering fluid", "Replace tie rods", "Perform alignment"],
                        "recommendation": "Regularly check steering system and keep fluid clean",
                        "emergency": True,
                        "risk_level": "high",
                        "dependencies": {
                            "if_yes": ["suspension_problems", "wheel_balance_problems"],
                            "if_no": ["clutch_problems", "brake_pad_problems"]
                        }
                    },
                    
                    "suspension_problems": {
                        "question": "Do you hear clunking sounds when going over bumps or turning?",
                        "why_reason": "Suspension problems affect ride comfort and vehicle stability",
                        "symptoms": ["Clunking sounds", "Vehicle vibration", "Uneven tire wear"],
                        "diagnosis_steps": [
                            "Check front and rear shock absorbers",
                            "Check bushings",
                            "Check control arms"
                        ],
                        "solutions": ["Replace shock absorbers", "Change bushings", "Adjust suspension"],
                        "recommendation": "Check suspension system every 20,000 km",
                        "emergency": False,
                        "risk_level": "medium",
                        "dependencies": {
                            "if_yes": ["wheel_balance_problems", "air_leak_problems"],
                            "if_no": ["steering_problems", "brake_pad_problems"]
                        }
                    }
                },
                
                # 6. Brake System
                "brake_system": {
                    "brake_pad_problems": {
                        "question": "Do you hear squealing when using brakes?",
                        "why_reason": "Squealing usually indicates worn brake pads",
                        "symptoms": ["Brake squealing", "Weak braking", "Pedal vibration"],
                        "diagnosis_steps": [
                            "Check brake pad thickness",
                            "Check disc or drum condition",
                            "Check brake fluid level"
                        ],
                        "solutions": ["Replace pads", "Repair discs", "Change brake fluid"],
                        "recommendation": "Replace brake pads when continuous squealing is heard",
                        "emergency": True,
                        "risk_level": "high",
                        "dependencies": {
                            "if_yes": ["brake_pedal_problems", "clutch_problems"],
                            "if_no": ["steering_problems", "suspension_problems"]
                        }
                    },
                    
                    "brake_pedal_problems": {
                        "question": "Is brake pedal spongy or goes to floor easily?",
                        "why_reason": "Spongy brake pedal indicates air in the system",
                        "symptoms": ["Spongy pedal", "Long stopping distance", "Pedal vibration"],
                        "diagnosis_steps": [
                            "Check brake fluid level",
                            "Check for system leaks",
                            "Bleed air from system"
                        ],
                        "solutions": ["Bleed air", "Change brake fluid", "Repair leaks"],
                        "recommendation": "Check brake system every 10,000 km",
                        "emergency": True,
                        "risk_level": "high",
                        "dependencies": {
                            "if_yes": ["brake_pad_problems", "steering_problems"],
                            "if_no": ["transmission_problems", "suspension_problems"]
                        }
                    }
                },
                
                # 7. Exhaust System
                "exhaust_system": {
                    "exhaust_problems": {
                        "question": "Do you hear loud exhaust noise or smell gases in the car?",
                        "why_reason": "Exhaust problems affect engine performance and environmental pollution",
                        "symptoms": ["Loud exhaust noise", "Gas smell", "Poor performance"],
                        "diagnosis_steps": [
                            "Check entire exhaust system for leaks",
                            "Check catalytic converter",
                            "Check oxygen sensor"
                        ],
                        "solutions": ["Repair leaks", "Replace catalytic converter", "Clean sensor"],
                        "recommendation": "Check exhaust system annually for leaks",
                        "emergency": False,
                        "risk_level": "medium",
                        "dependencies": {
                            "if_yes": ["oxygen_sensor_problems", "engine_problems"],
                            "if_no": ["fuel_system_problems", "cooling_system_problems"]
                        }
                    },
                    
                    "oxygen_sensor_problems": {
                        "question": "Is there excessive fuel consumption or weak engine power?",
                        "why_reason": "Oxygen sensor affects fuel-air mixture in engine",
                        "symptoms": ["Excessive fuel consumption", "Weak power", "Starting difficulty"],
                        "diagnosis_steps": [
                            "Read trouble codes with OBD2 scanner",
                            "Check oxygen sensor signal",
                            "Check electrical connections"
                        ],
                        "solutions": ["Clean sensor", "Replace oxygen sensor", "Check connections"],
                        "recommendation": "Replace oxygen sensor every 100,000 km",
                        "emergency": False,
                        "risk_level": "medium",
                        "dependencies": {
                            "if_yes": ["exhaust_problems", "fuel_injector_problems"],
                            "if_no": ["fuel_filter_problems", "spark_plug_problems"]
                        }
                    }
                },
                
                # 8. Tires and Wheels
                "tires_wheels": {
                    "air_leak_problems": {
                        "question": "Do tires lose air quickly or need frequent filling?",
                        "why_reason": "Air leaks affect fuel efficiency and driving safety",
                        "symptoms": ["Air loss", "Low pressure", "Uneven wear"],
                        "diagnosis_steps": [
                            "Check air pressure in all tires",
                            "Look for punctures or tire damage",
                            "Check valves and rims"
                        ],
                        "solutions": ["Repair punctures", "Replace valves", "Replace tire"],
                        "recommendation": "Check tire pressure weekly and before long trips",
                        "emergency": False,
                        "risk_level": "medium",
                        "dependencies": {
                            "if_yes": ["wheel_balance_problems", "suspension_problems"],
                            "if_no": ["brake_pad_problems", "steering_problems"]
                        }
                    },
                    
                    "wheel_balance_problems": {
                        "question": "Is there steering wheel vibration at high speeds?",
                        "why_reason": "Unbalanced wheels cause vibrations and affect driving safety",
                        "symptoms": ["Steering wheel vibration", "Uneven tire wear", "Humming sounds"],
                        "diagnosis_steps": [
                            "Check wheel balance on machine",
                            "Check wheel alignment",
                            "Check wheel bearings"
                        ],
                        "solutions": ["Balance wheels", "Adjust alignment", "Replace bearings"],
                        "recommendation": "Balance wheels every 10,000 km or when changing tires",
                        "emergency": False,
                        "risk_level": "medium",
                        "dependencies": {
                            "if_yes": ["air_leak_problems", "suspension_problems"],
                            "if_no": ["steering_problems", "brake_pad_problems"]
                        }
                    }
                },
                
                # 9. Air Conditioning and Heating
                "ac_heating": {
                    "ac_cooling_problems": {
                        "question": "Does air conditioning not cool sufficiently?",
                        "why_reason": "Poor cooling affects comfort while driving",
                        "symptoms": ["Air not cold", "Weak cooling", "Bad odors"],
                        "diagnosis_steps": [
                            "Check cabin air filter",
                            "Check refrigerant charge",
                            "Check compressor pressure"
                        ],
                        "solutions": ["Clean filter", "Recharge refrigerant", "Service compressor"],
                        "recommendation": "Clean AC filter every 6 months",
                        "emergency": False,
                        "risk_level": "low",
                        "dependencies": {
                            "if_yes": ["heating_problems", "alternator_problems"],
                            "if_no": ["cooling_system_problems", "battery_problems"]
                        }
                    },
                    
                    "heating_problems": {
                        "question": "Does heating system not work well in cold weather?",
                        "why_reason": "Heating system is important for comfort in cold weather driving",
                        "symptoms": ["Air not hot", "Weak heating", "Strange odors"],
                        "diagnosis_steps": [
                            "Check coolant level",
                            "Check heater valve",
                            "Check heater fans"
                        ],
                        "solutions": ["Add coolant", "Replace valve", "Clean ducts"],
                        "recommendation": "Check heating system before winter season",
                        "emergency": False,
                        "risk_level": "low",
                        "dependencies": {
                            "if_yes": ["ac_cooling_problems", "cooling_system_problems"],
                            "if_no": ["battery_problems", "electrical_system_problems"]
                        }
                    }
                },
                
                # 10. Safety Systems
                "safety_systems": {
                    "airbag_problems": {
                        "question": "Is airbag warning light on in dashboard?",
                        "why_reason": "Airbags are essential for protection in accidents",
                        "symptoms": ["Airbag warning light", "Airbags not working", "Warning sounds"],
                        "diagnosis_steps": [
                            "Read trouble codes with OBD2 scanner",
                            "Check airbag control unit",
                            "Check connections and sensors"
                        ],
                        "solutions": ["Reset system", "Replace sensors", "Service control unit"],
                        "recommendation": "Don't attempt airbag repairs yourself",
                        "emergency": True,
                        "risk_level": "high",
                        "dependencies": {
                            "if_yes": ["seatbelt_problems", "alarm_system_problems"],
                            "if_no": ["electrical_system_problems", "battery_problems"]
                        }
                    },
                    
                    "seatbelt_problems": {
                        "question": "Do seatbelts not work properly or get stuck?",
                        "why_reason": "Seatbelts are first line of defense in accidents",
                        "symptoms": ["Belts not locking", "Difficulty pulling", "Clicking sounds"],
                        "diagnosis_steps": [
                            "Check locking mechanism in belts",
                            "Check retractor mechanisms",
                            "Check electrical connections"
                        ],
                        "solutions": ["Clean mechanisms", "Replace belts", "Repair locking systems"],
                        "recommendation": "Regularly check seatbelts and ensure proper operation",
                        "emergency": True,
                        "risk_level": "high",
                        "dependencies": {
                            "if_yes": ["airbag_problems", "alarm_system_problems"],
                            "if_no": ["brake_pad_problems", "steering_problems"]
                        }
                    }
                },
                
                # 11. Fuel System
                "fuel_system": {
                    "fuel_filter_problems": {
                        "question": "Is there weak engine power or sudden stopping while driving?",
                        "why_reason": "Clogged fuel filter prevents fuel flow to engine",
                        "symptoms": ["Weak power", "Engine stopping", "Excessive fuel consumption"],
                        "diagnosis_steps": [
                            "Check fuel pressure",
                            "Check fuel filter",
                            "Check fuel pump"
                        ],
                        "solutions": ["Replace fuel filter", "Clean system", "Check pump"],
                        "recommendation": "Replace fuel filter every 20,000 km",
                        "emergency": False,
                        "risk_level": "medium",
                        "dependencies": {
                            "if_yes": ["fuel_injector_problems", "fuel_pump_problems"],
                            "if_no": ["spark_plug_problems", "engine_problems"]
                        }
                    },
                    
                    "fuel_injector_problems": {
                        "question": "Does engine run irregularly or have vibrations?",
                        "why_reason": "Clogged fuel injectors affect combustion efficiency",
                        "symptoms": ["Engine vibration", "Poor performance", "Excessive fuel consumption"],
                        "diagnosis_steps": [
                            "Check fuel injectors with diagnostic tool",
                            "Measure injection pressure",
                            "Check electrical connections"
                        ],
                        "solutions": ["Clean injectors", "Replace injectors", "Adjust pressure"],
                        "recommendation": "Use high-quality fuel and clean injectors regularly",
                        "emergency": False,
                        "risk_level": "medium",
                        "dependencies": {
                            "if_yes": ["fuel_filter_problems", "oxygen_sensor_problems"],
                            "if_no": ["spark_plug_problems", "cooling_system_problems"]
                        }
                    }
                }
            }
        }
        
        # نصوص الواجهة متعددة اللغات
        self.ui_texts = {
            "ar": {
                "welcome_title": "🚗 النظام الخبير الشامل لتشخيص أعطال السيارات 🚗",
                "welcome_message": "مرحباً بك في نظام التشخيص المتقدم!\nسأساعدك في تشخيص أعطال سيارتك خطوة بخطوة",
                "instructions": "إرشادات الاستخدام:\n- يمكنك الإجابة بـ 'نعم' أو 'لا' أو 'لماذا' لمعرفة سبب السؤال\n- للإجابة بـ 'خروج' في أي وقت لإنهاء البرنامج\n- للإجابة بـ 'رجوع' للعودة للسؤال السابق\n- للإجابة بـ 'تخطي' لتخطي السؤال الحالي",
                "start_diagnosis": "🔍 بدء عملية التشخيص الشاملة...",
                "checking_section": "📂 فحص قسم: {}",
                "problem_detected": "✅ تم اكتشاف: {}",
                "no_problems": "🎉 لم يتم العثور على أي أعطال واضحة!",
                "no_problems_msg": "بناءً على إجاباتك، لا يبدو أن هناك أعطالاً رئيسية.\nنوصي بالصيانة الدورية والفحص المنتظم للسيارة.",
                "results_title": "📊 نتائج التشخيص النهائية",
                "emergency_problems": "🚨 المشاكل الطارئة (تحتاج فحص فوري):",
                "high_risk_problems": "⚠️ المشاكل عالية الخطورة:",
                "medium_risk_problems": "📋 المشاكل متوسطة الخطورة:",
                "low_risk_problems": "ℹ️ المشاكل منخفضة الخطورة:",
                "explanation_title": "🧠 شرح آلية التفكير والتشخيص",
                "explanation_prompt": "🤔 هل تريد معرفة كيف توصلت إلى هذه النتائج؟ (نعم/لا): ",
                "report_title": "📄 تقرير التشخيص:",
                "new_session_prompt": "🔄 هل تريد بدء جلسة تشخيص جديدة؟ (نعم/لا): ",
                "goodbye": "شكراً لاستخدامك نظام التشخيص. نتمنى لك قيادة آمنة! 🚗💨",
                "invalid_input": "الإدخال غير صالح. الرجاء الاختيار من: {}",
                "cannot_go_back": "⚠️ لا يمكن الرجوع أكثر، هذه هي البداية",
                "category_names": {
                    "نظام_الطاقة": "نظام الطاقة والمحرك",
                    "النظام_الكهربائي": "النظام الكهربائي",
                    "نظام_التبريد": "نظام التبريد",
                    "نقل_الحركة": "نقل الحركة",
                    "التوجيه_والتعليق": "التوجيه والتعليق",
                    "نظام_الفرامل": "نظام الفرامل",
                    "نظام_العادم": "نظام العادم",
                    "الإطارات_والعجلات": "الإطارات والعجلات",
                    "التكييف_والتدفئة": "التكييف والتدفئة",
                    "أنظمة_السلامة": "أنظمة السلامة",
                    "نظام_الوقود": "نظام الوقود"
                }
            },
            "en": {
                "welcome_title": "🚗 Comprehensive Car Diagnostics Expert System 🚗",
                "welcome_message": "Welcome to the advanced diagnostic system!\nI will help you diagnose your car problems step by step",
                "instructions": "Usage Instructions:\n- You can answer with 'yes' or 'no' or 'why' to know the reason for the question\n- Type 'exit' at any time to end the program\n- Type 'back' to return to previous question\n- Type 'skip' to skip current question",
                "start_diagnosis": "🔍 Starting comprehensive diagnosis process...",
                "checking_section": "📂 Checking section: {}",
                "problem_detected": "✅ Detected: {}",
                "no_problems": "🎉 No obvious problems found!",
                "no_problems_msg": "Based on your answers, there don't seem to be any major problems.\nWe recommend regular maintenance and periodic vehicle inspection.",
                "results_title": "📊 Final Diagnosis Results",
                "emergency_problems": "🚨 Emergency Problems (Need immediate inspection):",
                "high_risk_problems": "⚠️ High Risk Problems:",
                "medium_risk_problems": "📋 Medium Risk Problems:",
                "low_risk_problems": "ℹ️ Low Risk Problems:",
                "explanation_title": "🧠 Explanation of Reasoning and Diagnosis",
                "explanation_prompt": "🤔 Would you like to know how I reached these conclusions? (yes/no): ",
                "report_title": "📄 Diagnosis Report:",
                "new_session_prompt": "🔄 Would you like to start a new diagnosis session? (yes/no): ",
                "goodbye": "Thank you for using the diagnostic system. Wishing you safe driving! 🚗💨",
                "invalid_input": "Invalid input. Please choose from: {}",
                "cannot_go_back": "⚠️ Cannot go back further, this is the beginning",
                "category_names": {
                    "power_system": "Power and Engine System",
                    "electrical_system": "Electrical System",
                    "cooling_system": "Cooling System",
                    "transmission_system": "Transmission System",
                    "steering_suspension": "Steering and Suspension",
                    "brake_system": "Brake System",
                    "exhaust_system": "Exhaust System",
                    "tires_wheels": "Tires and Wheels",
                    "ac_heating": "Air Conditioning and Heating",
                    "safety_systems": "Safety Systems",
                    "fuel_system": "Fuel System"
                }
            }
        }
        
        self.current_language = None
        self.findings = []
        self.asked_questions = []
        self.current_category_index = 0
        self.current_problem_index = 0
        self.categories_map = {
            "ar": list(self.knowledge_base["ar"].keys()),
            "en": list(self.knowledge_base["en"].keys())
        }
        
class CarExpertSystemGUI:
    def __init__(self, root, expert_system):
        self.root = root
        self.expert_system = expert_system
        self.current_language = None
        self.selected_categories = []  # Store selected categories
        self.question_queue = []  # Queue for questions based on dependencies
        self.asked_questions = set()  # Track asked questions to avoid duplicates
        
        # Tab texts dictionary
        self.tab_texts = {
            "ar": ["الرئيسية", "التشخيص", "النتائج", "التقرير"],
            "en": ["Dashboard", "Diagnostics", "Results", "Report"]
        }
        
        self.setup_main_window()
        self.show_language_selection()
    
    def setup_main_window(self):
        """Setup the main window"""
        self.root.title("Car Expert System - Diagnosis System")
        self.root.geometry("1200x800")
        self.root.configure(bg="#f0f0f0")
        self.root.minsize(1000, 700)
        
        # Create notebook for tabs
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Create frames for each tab
        self.setup_welcome_frame()
        self.setup_diagnosis_frame()
        self.setup_results_frame()
        self.setup_report_frame()
        
        # Hide all tabs except welcome until language is selected
        self.notebook.hide(1)
        self.notebook.hide(2)
        self.notebook.hide(3)
        
    def setup_welcome_frame(self):
        """Setup welcome/dashboard frame"""
        self.welcome_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.welcome_frame, text="Welcome")
        
        # Welcome title
        self.welcome_label = tk.Label(self.welcome_frame, 
                            text="🚗 Car Diagnostics Expert System 🚗",
                            font=("Arial", 18, "bold"),
                            fg="#2c3e50",
                            bg="#f0f0f0",
                            justify="center")
        self.welcome_label.pack(pady=20)
        
        # Welcome message
        self.welcome_msg = tk.Label(self.welcome_frame,
                          text="Welcome to the advanced diagnostic system!\nI will help you diagnose your car problems step by step",
                          font=("Arial", 14),
                          fg="#34495e",
                          bg="#f0f0f0",
                          justify="center")
        self.welcome_msg.pack(pady=10)
        
        # Car icon
        car_icon = tk.Label(self.welcome_frame, text="🚗", font=("Arial", 50), bg="#f0f0f0")
        car_icon.pack(pady=20)
        
        # Language selection frame
        language_frame = tk.Frame(self.welcome_frame, bg="#f0f0f0")
        language_frame.pack(pady=20)
        
        # Arabic button
        self.arabic_button = tk.Button(language_frame,
                             text="العربية",
                             font=("Arial", 14, "bold"),
                             bg="#2c3e50",
                             fg="white",
                             command=lambda: self.set_language("ar"),
                             width=15,
                             height=2)
        self.arabic_button.pack(side=tk.RIGHT, padx=10)
        
        # English button
        self.english_button = tk.Button(language_frame,
                                text="English",
                                font=("Arial", 14, "bold"),
                                bg="#3498db",
                                fg="white",
                                command=lambda: self.set_language("en"),
                                width=15,
                                height=2)
        self.english_button.pack(side=tk.LEFT, padx=10)
        
        # Exit button
        self.exit_button = tk.Button(self.welcome_frame,
                                text="Exit",
                                font=("Arial", 12),
                                bg="#e74c3c",
                                fg="white",
                                command=self.exit_program,
                                width=15,
                                height=1)
        self.exit_button.pack(pady=20)
    
    def setup_diagnosis_frame(self):
        """Setup diagnosis frame"""
        self.diagnosis_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.diagnosis_frame, text="Diagnostics")
        
        # Question section
        question_frame = tk.Frame(self.diagnosis_frame, bg="#ffffff", relief=tk.GROOVE, bd=2)
        question_frame.pack(fill="x", padx=10, pady=10)
        
        self.question_label = tk.Label(question_frame,
                                      text="Question will appear here",
                                      font=("Arial", 14),
                                      wraplength=800,
                                      justify="center",
                                      bg="#ffffff")
        self.question_label.pack(pady=20, padx=20)
        
        # Button section
        button_frame = tk.Frame(self.diagnosis_frame, bg="#f0f0f0")
        button_frame.pack(pady=20)
        
        self.yes_button = tk.Button(button_frame,
                                   text="Yes",
                                   font=("Arial", 12, "bold"),
                                   bg="#2ecc71",
                                   fg="white",
                                   command=lambda: self.answer_question(True),
                                   width=10,
                                   height=2)
        self.yes_button.grid(row=0, column=0, padx=10)
        
        self.no_button = tk.Button(button_frame,
                                  text="No",
                                  font=("Arial", 12, "bold"),
                                  bg="#e74c3c",
                                  fg="white",
                                  command=lambda: self.answer_question(False),
                                  width=10,
                                  height=2)
        self.no_button.grid(row=0, column=1, padx=10)
        
        self.why_button = tk.Button(button_frame,
                                   text="Why",
                                   font=("Arial", 12),
                                   bg="#3498db",
                                   fg="white",
                                   command=self.show_why_reason,
                                   width=10,
                                   height=2)
        self.why_button.grid(row=0, column=2, padx=10)
        
        # Navigation buttons
        nav_frame = tk.Frame(self.diagnosis_frame, bg="#f0f0f0")
        nav_frame.pack(pady=10)
        
        self.back_button = tk.Button(nav_frame,
                                    text="Back",
                                    font=("Arial", 10),
                                    bg="#f39c12",
                                    fg="white",
                                    command=self.go_back,
                                    width=8)
        self.back_button.pack(side=tk.LEFT, padx=5)
        
        self.skip_button = tk.Button(nav_frame,
                                    text="Skip",
                                    font=("Arial", 10),
                                    bg="#95a5a6",
                                    fg="white",
                                    command=self.skip_question,
                                    width=8)
        self.skip_button.pack(side=tk.LEFT, padx=5)
        
        self.exit_diagnosis_button = tk.Button(nav_frame,
                                    text="Exit",
                                    font=("Arial", 10),
                                    bg="#7f8c8d",
                                    fg="white",
                                    command=self.exit_program,
                                    width=8)
        self.exit_diagnosis_button.pack(side=tk.LEFT, padx=5)
        
        # Current question info
        info_frame = tk.Frame(self.diagnosis_frame, bg="#f9f9f9", relief=tk.GROOVE, bd=1)
        info_frame.pack(fill="x", padx=10, pady=10)
        
        self.current_section_label = tk.Label(info_frame,
                                             text="Section: ",
                                             font=("Arial", 10),
                                             bg="#f9f9f9")
        self.current_section_label.pack(anchor="w", padx=10, pady=5)
        
        self.current_problem_label = tk.Label(info_frame,
                                             text="Problem: ",
                                             font=("Arial", 10),
                                             bg="#f9f9f9")
        self.current_problem_label.pack(anchor="w", padx=10, pady=5)
        
        self.progress_label = tk.Label(info_frame,
                                      text="Progress: 0/0",
                                      font=("Arial", 10),
                                      bg="#f9f9f9")
        self.progress_label.pack(anchor="w", padx=10, pady=5)
    
    def setup_results_frame(self):
        """Setup results frame"""
        self.results_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.results_frame, text="Results")
        
        # Create scrollable results area
        results_canvas = tk.Canvas(self.results_frame, bg="#f0f0f0")
        scrollbar = ttk.Scrollbar(self.results_frame, orient="vertical", command=results_canvas.yview)
        self.scrollable_results_frame = ttk.Frame(results_canvas)
        
        self.scrollable_results_frame.bind(
            "<Configure>",
            lambda e: results_canvas.configure(scrollregion=results_canvas.bbox("all"))
        )
        
        results_canvas.create_window((0, 0), window=self.scrollable_results_frame, anchor="nw")
        results_canvas.configure(yscrollcommand=scrollbar.set)
        
        results_canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Results title
        self.results_title = tk.Label(self.scrollable_results_frame,
                                text="Diagnosis Results",
                                font=("Arial", 16, "bold"),
                                fg="#2c3e50")
        self.results_title.pack(pady=10)
        
        # Create tabbed results
        self.results_notebook = ttk.Notebook(self.scrollable_results_frame)
        self.results_notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Frames for different result types
        self.emergency_frame = ttk.Frame(self.results_notebook)
        self.high_risk_frame = ttk.Frame(self.results_notebook)
        self.medium_risk_frame = ttk.Frame(self.results_notebook)
        self.low_risk_frame = ttk.Frame(self.results_notebook)
        self.no_problems_frame = ttk.Frame(self.results_notebook)
        
        self.results_notebook.add(self.emergency_frame, text="Emergency Problems")
        self.results_notebook.add(self.high_risk_frame, text="High Risk Problems")
        self.results_notebook.add(self.medium_risk_frame, text="Medium Risk Problems")
        self.results_notebook.add(self.low_risk_frame, text="Low Risk Problems")
        self.results_notebook.add(self.no_problems_frame, text="No Problems")
        
        # Setup scrollable frames
        self.setup_scrollable_frame(self.emergency_frame)
        self.setup_scrollable_frame(self.high_risk_frame)
        self.setup_scrollable_frame(self.medium_risk_frame)
        self.setup_scrollable_frame(self.low_risk_frame)
        
        # No problems frame setup
        self.no_problems_label = tk.Label(self.no_problems_frame,
                                    text="🎉 No obvious problems found!",
                                    font=("Arial", 14),
                                    fg="#27ae60")
        self.no_problems_label.pack(pady=20)
        
        self.no_problems_msg = tk.Label(self.no_problems_frame,
                                  text="Based on your answers, there don't seem to be any major problems.\nWe recommend regular maintenance and periodic vehicle inspection.",
                                  font=("Arial", 12),
                                  justify="center")
        self.no_problems_msg.pack(pady=10)
        
        # Report button
        self.report_button = tk.Button(self.scrollable_results_frame,
                                text="View Detailed Report",
                                font=("Arial", 12),
                                bg="#3498db",
                                fg="white",
                                command=self.show_report,
                                padx=15,
                                pady=8)
        self.report_button.pack(pady=10)
        
        # Explanation button
        self.explanation_button = tk.Button(self.scrollable_results_frame,
                                text="How I Reached These Results",
                                font=("Arial", 12),
                                bg="#9b59b6",
                                fg="white",
                                command=self.show_explanation,
                                padx=15,
                                pady=8)
        self.explanation_button.pack(pady=10)
        
        # New diagnosis button
        self.new_diagnosis_button = tk.Button(self.scrollable_results_frame,
                                        text="Start New Diagnosis",
                                        font=("Arial", 12),
                                        bg="#2ecc71",
                                        fg="white",
                                        command=self.start_new_diagnosis,
                                        padx=15,
                                        pady=8)
        self.new_diagnosis_button.pack(pady=5)
    
    def setup_scrollable_frame(self, parent_frame):
        """Setup a scrollable frame"""
        canvas = tk.Canvas(parent_frame)
        scrollbar = ttk.Scrollbar(parent_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        return scrollable_frame
    
    def setup_report_frame(self):
        """Setup report frame"""
        self.report_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.report_frame, text="Report")
        
        # Report title
        self.report_title = tk.Label(self.report_frame,
                               text="Detailed Diagnosis Report",
                               font=("Arial", 16, "bold"),
                               fg="#2c3e50")
        self.report_title.pack(pady=10)
        
        # Report text area
        self.report_text = scrolledtext.ScrolledText(self.report_frame,
                                                   wrap=tk.WORD,
                                                   width=100,
                                                   height=30,
                                                   font=("Arial", 11))
        self.report_text.pack(padx=10, pady=10, fill="both", expand=True)
        
        # Control buttons
        button_frame = tk.Frame(self.report_frame)
        button_frame.pack(pady=10)
        
        self.save_button = tk.Button(button_frame,
                               text="Save Report",
                               font=("Arial", 12),
                               bg="#3498db",
                               fg="white",
                               command=self.save_report,
                               padx=15,
                               pady=5)
        self.save_button.pack(side=tk.LEFT, padx=10)
        
        self.print_button = tk.Button(button_frame,
                                text="Print Report",
                                font=("Arial", 12),
                                bg="#2ecc71",
                                fg="white",
                                command=self.print_report,
                                padx=15,
                                pady=5)
        self.print_button.pack(side=tk.LEFT, padx=10)
        
        self.back_button_report = tk.Button(button_frame,
                               text="Back to Results",
                               font=("Arial", 12),
                               bg="#95a5a6",
                               fg="white",
                               command=self.back_to_results,
                               padx=15,
                               pady=5)
        self.back_button_report.pack(side=tk.LEFT, padx=10)
    
    def show_language_selection(self):
        """Show language selection screen"""
        self.notebook.select(0)
    
    def set_language(self, language):
        """Set the selected language"""
        self.current_language = language
        self.expert_system.current_language = language
        self.update_ui_texts()
        
        # Update tab texts
        for i, text in enumerate(self.tab_texts[language]):
            self.notebook.tab(i, text=text)
        
        # Go to diagnosis tab after language selection
        self.notebook.select(1)
        
        # Start diagnosis process
        self.start_diagnosis()
    
    def update_ui_texts(self):
        """Update UI texts based on selected language"""
        if not self.current_language:
            return
            
        texts = self.expert_system.ui_texts[self.current_language]
        
        # Update tab texts
        for i, text in enumerate(self.tab_texts[self.current_language]):
            self.notebook.tab(i, text=text)
        
        # Update welcome frame
        if self.current_language == "ar":
            self.welcome_label.config(text="🚗 النظام الخبير الشامل لتشخيص أعطال السيارات 🚗")
            self.welcome_msg.config(text="مرحباً بك في نظام التشخيص المتقدم!\nسأساعدك في تشخيص أعطال سيارتك خطوة بخطوة")
            self.exit_button.config(text="خروج")
        else:
            self.welcome_label.config(text="🚗 Comprehensive Car Diagnostics Expert System 🚗")
            self.welcome_msg.config(text="Welcome to the advanced diagnostic system!\nI will help you diagnose your car problems step by step")
            self.exit_button.config(text="Exit")
        
        # Update diagnosis frame
        if self.current_language == "ar":
            self.yes_button.config(text="نعم")
            self.no_button.config(text="لا")
            self.why_button.config(text="لماذا")
            self.back_button.config(text="رجوع")
            self.skip_button.config(text="تخطي")
            self.exit_diagnosis_button.config(text="خروج")
        else:
            self.yes_button.config(text="Yes")
            self.no_button.config(text="No")
            self.why_button.config(text="Why")
            self.back_button.config(text="Back")
            self.skip_button.config(text="Skip")
            self.exit_diagnosis_button.config(text="Exit")
        
        # Update results frame
        if self.current_language == "ar":
            self.results_title.config(text="نتائج التشخيص")
            self.results_notebook.tab(0, text="المشاكل الطارئة")
            self.results_notebook.tab(1, text="المشاكل عالية الخطورة")
            self.results_notebook.tab(2, text="المشاكل متوسطة الخطورة")
            self.results_notebook.tab(3, text="المشاكل منخفضة الخطورة")
            self.results_notebook.tab(4, text="لا توجد مشاكل")
            self.no_problems_label.config(text="🎉 لم يتم العثور على أي أعطال واضحة!")
            self.no_problems_msg.config(text="بناءً على إجاباتك، لا يبدو أن هناك أعطالاً رئيسية.\nنوصي بالصيانة الدورية والفحص المنتظم للسيارة.")
            self.report_button.config(text="عرض التقرير المفصل")
            self.explanation_button.config(text="كيف وصلت لهذه النتائج")
            self.new_diagnosis_button.config(text="بدء تشخيص جديد")
        else:
            self.results_title.config(text="Diagnosis Results")
            self.results_notebook.tab(0, text="Emergency Problems")
            self.results_notebook.tab(1, text="High Risk Problems")
            self.results_notebook.tab(2, text="Medium Risk Problems")
            self.results_notebook.tab(3, text="Low Risk Problems")
            self.results_notebook.tab(4, text="No Problems")
            self.no_problems_label.config(text="🎉 No obvious problems found!")
            self.no_problems_msg.config(text="Based on your answers, there don't seem to be any major problems.\nWe recommend regular maintenance and periodic vehicle inspection.")
            self.report_button.config(text="View Detailed Report")
            self.explanation_button.config(text="How I Reached These Results")
            self.new_diagnosis_button.config(text="Start New Diagnosis")
        
        # Update report frame
        if self.current_language == "ar":
            self.report_title.config(text="تقرير التشخيص المفصل")
            self.save_button.config(text="حفظ التقرير")
            self.print_button.config(text="طباعة التقرير")
            self.back_button_report.config(text="العودة إلى النتائج")
        else:
            self.report_title.config(text="Detailed Diagnosis Report")
            self.save_button.config(text="Save Report")
            self.print_button.config(text="Print Report")
            self.back_button_report.config(text="Back to Results")
    
    def start_diagnosis(self):
        """Start diagnosis process with section selection"""
        # Initialize diagnosis process
        self.expert_system.findings = []
        self.expert_system.asked_questions = []
        self.question_queue = []
        self.asked_questions = set()
        
        # Show category selection options to user
        self.ask_for_category_selection()
    
    def ask_for_category_selection(self):
        """Ask user to select diagnostic sections with checkboxes"""
        # Create category selection window
        self.category_window = tk.Toplevel(self.root)
        self.category_window.title("Select Diagnosis Sections" if self.current_language == "en" else "اختر أقسام التشخيص")
        self.category_window.geometry("700x600")
        self.category_window.configure(bg="#f0f0f0")
        self.category_window.grab_set()  # Make it modal
        
        # Window title
        title_label = tk.Label(self.category_window,
                            text="Select Diagnosis Sections" if self.current_language == "en" else "اختر أقسام التشخيص",
                            font=("Arial", 16, "bold"),
                            bg="#f0f0f0",
                            fg="#2c3e50")
        title_label.pack(pady=20)
        
        # Explanation
        explanation_label = tk.Label(self.category_window,
                                text="Select the sections you want to diagnose (check boxes)" if self.current_language == "en" else "اختر الأقسام التي تريد تشخيصها (حدد المربعات)",
                                font=("Arial", 12),
                                bg="#f0f0f0",
                                fg="#34495e")
        explanation_label.pack(pady=10)
        
        # Create scrollable frame for categories
        canvas = tk.Canvas(self.category_window)
        scrollbar = ttk.Scrollbar(self.category_window, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True, padx=10, pady=10)
        scrollbar.pack(side="right", fill="y")
        
        # Select all checkbox
        self.select_all_var = tk.BooleanVar()
        select_all_check = tk.Checkbutton(scrollable_frame,
                                        text="Select All Sections" if self.current_language == "en" else "اختيار جميع الأقسام",
                                        font=("Arial", 12, "bold"),
                                        variable=self.select_all_var,
                                        command=self.toggle_select_all,
                                        bg="#f0f0f0")
        select_all_check.pack(anchor="w", pady=10, padx=10)
        
        # Category checkboxes
        self.category_vars = {}
        for category_key in self.expert_system.categories_map[self.current_language]:
            category_name = self.expert_system.ui_texts[self.current_language]["category_names"].get(category_key, category_key)
            
            var = tk.BooleanVar()
            self.category_vars[category_key] = var
            
            check = tk.Checkbutton(scrollable_frame,
                                text=category_name,
                                font=("Arial", 11),
                                variable=var,
                                bg="#f0f0f0")
            check.pack(anchor="w", pady=5, padx=30)
        
        # Buttons frame
        buttons_frame = tk.Frame(self.category_window, bg="#f0f0f0")
        buttons_frame.pack(pady=20)
        
        # Start diagnosis button
        start_button = tk.Button(buttons_frame,
                            text="Start Diagnosis" if self.current_language == "en" else "بدء التشخيص",
                            font=("Arial", 12),
                            bg="#2ecc71",
                            fg="white",
                            command=self.process_category_selection,
                            width=20,
                            height=2)
        start_button.pack(side=tk.LEFT, padx=10)
        
        # Cancel button
        cancel_button = tk.Button(buttons_frame,
                            text="Cancel" if self.current_language == "en" else "إلغاء",
                            font=("Arial", 12),
                            bg="#e74c3c",
                            fg="white",
                            command=self.category_window.destroy,
                            width=20,
                            height=2)
        cancel_button.pack(side=tk.LEFT, padx=10)
    def toggle_select_all(self):
        """Toggle selection of all categories"""
        select_all = self.select_all_var.get()
        for var in self.category_vars.values():
            var.set(select_all)
    
    def process_category_selection(self):
        """Process the selected categories and start diagnosis"""
        self.selected_categories = []
        
        for category_key, var in self.category_vars.items():
            if var.get():
                self.selected_categories.append(category_key)
        
        if not self.selected_categories:
            messagebox.showwarning("Warning" if self.current_language == "en" else "تحذير", 
                                 "Please select at least one section" if self.current_language == "en" else "الرجاء اختيار قسم واحد على الأقل")
            return
        
        self.category_window.destroy()
        self.initialize_question_queue()
        self.ask_next_question()
    
    def initialize_question_queue(self):
        """Initialize question queue based on selected categories and dependencies"""
        self.question_queue = []
        
        # Add starting questions from each selected category
        for category in self.selected_categories:
            problems = list(self.expert_system.knowledge_base[self.current_language][category].keys())
            if problems:
                self.question_queue.append((category, problems[0]))
    
    def start_full_diagnosis(self, window):
        """Start diagnosis of all sections"""
        window.destroy()
        self.expert_system.current_category_index = 0
        self.ask_next_question()
    
    def start_specific_diagnosis(self, category, window):
        """Start diagnosis of specific section"""
        window.destroy()
        # Find index of selected category
        categories = self.expert_system.categories_map[self.current_language]
        if category in categories:
            self.expert_system.current_category_index = categories.index(category)
        self.ask_next_question()
    
    def ask_next_question(self):
        """Ask the next question from the queue"""
        if not self.question_queue:
            # No more questions, show results
            self.show_results()
            return
        
        # Get next question from queue
        category, problem = self.question_queue.pop(0)
        
        # Skip if already asked
        if (category, problem) in self.asked_questions:
            self.ask_next_question()
            return
        
        self.asked_questions.add((category, problem))
        
        problem_data = self.expert_system.knowledge_base[self.current_language][category][problem]
        
        # Update UI with current question
        self.question_label.config(text=problem_data["question"])
        
        # Update current question info
        category_name = self.expert_system.ui_texts[self.current_language]["category_names"].get(category, category)
        self.current_section_label.config(text=f"{'Section' if self.current_language == 'en' else 'القسم'}: {category_name}")
        self.current_problem_label.config(text=f"{'Problem' if self.current_language == 'en' else 'المشكلة'}: {problem}")
        
        # Update progress
        total_questions = len(self.question_queue) + len(self.asked_questions)
        completed_questions = len(self.asked_questions)
        self.progress_label.config(text=f"{'Progress' if self.current_language == 'en' else 'التقدم'}: {completed_questions}/{total_questions}")
        
        # Store current question info for dependency handling
        self.current_category = category
        self.current_problem = problem
        self.current_problem_data = problem_data
    
    def answer_question(self, answer):
        """Process user answer and handle dependencies"""
        if answer:
            # Add problem to findings if answer is yes
            self.expert_system.findings.append({
                'category': self.current_category,
                'problem': self.current_problem,
                'data': self.current_problem_data
            })
            
            # Add dependent questions based on "if_yes" dependencies
            if 'dependencies' in self.current_problem_data and 'if_yes' in self.current_problem_data['dependencies']:
                for next_problem in self.current_problem_data['dependencies']['if_yes']:
                    # Find which category this problem belongs to
                    for cat in self.selected_categories:
                        if next_problem in self.expert_system.knowledge_base[self.current_language][cat]:
                            if (cat, next_problem) not in self.asked_questions:
                                self.question_queue.append((cat, next_problem))
                            break
        
        else:
            # Add alternative questions based on "if_no" dependencies
            if 'dependencies' in self.current_problem_data and 'if_no' in self.current_problem_data['dependencies']:
                for next_problem in self.current_problem_data['dependencies']['if_no']:
                    # Find which category this problem belongs to
                    for cat in self.selected_categories:
                        if next_problem in self.expert_system.knowledge_base[self.current_language][cat]:
                            if (cat, next_problem) not in self.asked_questions:
                                self.question_queue.append((cat, next_problem))
                            break
        
        # Store question info for tracking
        question_info = {
            "category": self.current_category,
            "problem": self.current_problem,
            "question": self.current_problem_data["question"],
            "why_reason": self.current_problem_data["why_reason"],
            "answer": answer
        }
        self.expert_system.asked_questions.append(question_info)
        
        # Ask next question
        self.ask_next_question()
    def show_why_reason(self):
        """Show reason for the question"""
        category = self.expert_system.categories_map[self.current_language][self.expert_system.current_category_index]
        problems = list(self.expert_system.knowledge_base[self.current_language][category].keys())
        problem_name = problems[self.expert_system.current_problem_index]
        why_reason = self.expert_system.knowledge_base[self.current_language][category][problem_name]["why_reason"]
        
        messagebox.showinfo("Reason for Question" if self.current_language == "en" else "سبب السؤال", why_reason)
    
    def go_back(self):
        """Go back to previous question - simplified for dependency system"""
        if len(self.expert_system.asked_questions) > 0:
            # Get info about previous question
            last_question = self.expert_system.asked_questions.pop()
            
            # If answering the last question added a problem, remove it
            if (last_question["answer"] and self.expert_system.findings and 
                self.expert_system.findings[-1]['problem'] == last_question['problem']):
                self.expert_system.findings.pop()
            
            # Remove from asked questions set
            self.asked_questions.discard((last_question["category"], last_question["problem"]))
            
            # Re-ask the previous question
            self.question_queue.insert(0, (last_question["category"], last_question["problem"]))
            self.ask_next_question()
        else:
            messagebox.showinfo("Information" if self.current_language == "en" else "معلومة", 
                               "Cannot go back further" if self.current_language == "en" else "لا يمكن الرجوع أكثر")
    def skip_question(self):
        """Skip current question"""
        # Add to asked questions without processing dependencies
        self.asked_questions.add((self.current_category, self.current_problem))
        
        # Store question info
        question_info = {
            "category": self.current_category,
            "problem": self.current_problem,
            "question": self.current_problem_data["question"],
            "why_reason": self.current_problem_data["why_reason"],
            "answer": None,
            "skipped": True
        }
        self.expert_system.asked_questions.append(question_info)
        
        # Ask next question
        self.ask_next_question()
    
    def show_results(self):
        """Show diagnosis results"""
        # Go to results tab
        self.notebook.select(2)
        
        # Clear old content from scrollable frames
        for frame in [self.emergency_frame, self.high_risk_frame, self.medium_risk_frame, self.low_risk_frame]:
            for widget in frame.winfo_children():
                widget.destroy()
        
        # Recreate scrollable frames
        emergency_scrollable = self.setup_scrollable_frame(self.emergency_frame)
        high_risk_scrollable = self.setup_scrollable_frame(self.high_risk_frame)
        medium_risk_scrollable = self.setup_scrollable_frame(self.medium_risk_frame)
        low_risk_scrollable = self.setup_scrollable_frame(self.low_risk_frame)
        
        # Categorize results by risk level
        emergency_problems = []
        high_risk_problems = []
        medium_risk_problems = []
        low_risk_problems = []
        
        for finding in self.expert_system.findings:
            problem_data = finding['data']
            if problem_data['emergency']:
                emergency_problems.append(finding)
            elif problem_data['risk_level'] in ['عالي', 'high']:
                high_risk_problems.append(finding)
            elif problem_data['risk_level'] in ['متوسط', 'medium']:
                medium_risk_problems.append(finding)
            else:
                low_risk_problems.append(finding)
        
        # Show emergency problems
        if emergency_problems:
            self.display_problems_in_frame(emergency_scrollable, emergency_problems, "🚨")
        else:
            no_emergency_label = tk.Label(emergency_scrollable, 
                                         text="No emergency problems" if self.current_language == "en" else "لا توجد مشاكل طارئة",
                                         font=("Arial", 12),
                                         fg="#27ae60")
            no_emergency_label.pack(pady=20)
        
        # Show high risk problems
        if high_risk_problems:
            self.display_problems_in_frame(high_risk_scrollable, high_risk_problems, "⚠️")
        else:
            no_high_risk_label = tk.Label(high_risk_scrollable, 
                                         text="No high risk problems" if self.current_language == "en" else "لا توجد مشاكل عالية الخطورة",
                                         font=("Arial", 12),
                                         fg="#27ae60")
            no_high_risk_label.pack(pady=20)
        
        # Show medium risk problems
        if medium_risk_problems:
            self.display_problems_in_frame(medium_risk_scrollable, medium_risk_problems, "📋")
        else:
            no_medium_risk_label = tk.Label(medium_risk_scrollable, 
                                           text="No medium risk problems" if self.current_language == "en" else "لا توجد مشاكل متوسطة الخطورة",
                                           font=("Arial", 12),
                                           fg="#27ae60")
            no_medium_risk_label.pack(pady=20)
        
        # Show low risk problems
        if low_risk_problems:
            self.display_problems_in_frame(low_risk_scrollable, low_risk_problems, "ℹ️")
        else:
            no_low_risk_label = tk.Label(low_risk_scrollable, 
                                        text="No low risk problems" if self.current_language == "en" else "لا توجد مشاكل منخفضة الخطورة",
                                        font=("Arial", 12),
                                        fg="#27ae60")
            no_low_risk_label.pack(pady=20)
        
        # Hide "No problems" frame if there are problems
        if self.expert_system.findings:
            self.results_notebook.hide(4)
        else:
            self.results_notebook.select(4)
    
    def display_problems_in_frame(self, frame, problems, emoji):
        """Display problems in the specified frame"""
        for i, finding in enumerate(problems):
            problem_data = finding['data']
            category_name = self.expert_system.ui_texts[self.current_language]["category_names"].get(finding['category'], finding['category'])
            
            # Create frame for each problem
            problem_frame = tk.Frame(frame, bg="#f9f9f9", relief=tk.GROOVE, bd=1)
            problem_frame.pack(fill="x", padx=10, pady=5)
            
            # Problem title
            problem_title = tk.Label(problem_frame,
                                    text=f"{emoji} {finding['problem']}",
                                    font=("Arial", 12, "bold"),
                                    bg="#f9f9f9")
            problem_title.pack(anchor="w", padx=10, pady=5)
            
            # Problem section
            category_label = tk.Label(problem_frame,
                                     text=f"📍 {'Section' if self.current_language == 'en' else 'القسم'}: {category_name}",
                                     font=("Arial", 10),
                                     bg="#f9f9f9")
            category_label.pack(anchor="w", padx=10, pady=2)
            
            # Symptoms
            symptoms_label = tk.Label(problem_frame,
                                     text=f"🎯 {'Symptoms' if self.current_language == 'en' else 'الأعراض'}: {', '.join(problem_data['symptoms'])}",
                                     font=("Arial", 10),
                                     bg="#f9f9f9")
            symptoms_label.pack(anchor="w", padx=10, pady=2)
            
            # Diagnosis steps
            diagnosis_label = tk.Label(problem_frame,
                                      text=f"🔧 {'Diagnosis Steps' if self.current_language == 'en' else 'خطوات التشخيص'}:",
                                      font=("Arial", 10, "bold"),
                                      bg="#f9f9f9")
            diagnosis_label.pack(anchor="w", padx=10, pady=5)
            
            for j, step in enumerate(problem_data['diagnosis_steps'], 1):
                step_label = tk.Label(problem_frame,
                                     text=f"   {j}. {step}",
                                     font=("Arial", 9),
                                     bg="#f9f9f9",
                                     justify="left")
                step_label.pack(anchor="w", padx=20, pady=1)
            
            # Suggested solutions
            solutions_label = tk.Label(problem_frame,
                                      text=f"💡 {'Suggested Solutions' if self.current_language == 'en' else 'الحلول المقترحة'}:",
                                      font=("Arial", 10, "bold"),
                                      bg="#f9f9f9")
            solutions_label.pack(anchor="w", padx=10, pady=5)
            
            for j, solution in enumerate(problem_data['solutions'], 1):
                solution_label = tk.Label(problem_frame,
                                         text=f"   {j}. {solution}",
                                         font=("Arial", 9),
                                         bg="#f9f9f9",
                                         justify="left")
                solution_label.pack(anchor="w", padx=20, pady=1)
            
            # Recommendation
            recommendation_label = tk.Label(problem_frame,
                                           text=f"📝 {'Recommendation' if self.current_language == 'en' else 'التوصية'}: {problem_data['recommendation']}",
                                           font=("Arial", 10),
                                           bg="#f9f9f9")
            recommendation_label.pack(anchor="w", padx=10, pady=5)
            
            # Risk level
            risk_label = tk.Label(problem_frame,
                                 text=f"⚠️ {'Risk Level' if self.current_language == 'en' else 'مستوى الخطورة'}: {problem_data['risk_level']}",
                                 font=("Arial", 10),
                                 bg="#f9f9f9")
            risk_label.pack(anchor="w", padx=10, pady=5)
    
    def show_report(self):
        """Show detailed report"""
        # Go to report tab
        self.notebook.select(3)
        
        # Generate report
        report_text = self.generate_report()
        
        # Display report in text area
        self.report_text.delete(1.0, tk.END)
        self.report_text.insert(tk.END, report_text)
    
    def generate_report(self):
        """Generate diagnosis report"""
        if not self.expert_system.findings:
            return "No problems detected." if self.current_language == "en" else "لم يتم اكتشاف أي أعطال."
        
        if self.current_language == "en":
            report = "Car Diagnostics Report\n"
            report += "=" * 40 + "\n\n"
            report += f"Diagnosis Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n"  # FIXED
            report += f"Problems Found: {len(self.expert_system.findings)}\n\n"
        else:
            report = "تقرير تشخيص أعطال السيارات\n"
            report += "=" * 40 + "\n\n"
            report += f"تاريخ التشخيص: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n"  # FIXED
            report += f"عدد الأعطال المكتشفة: {len(self.expert_system.findings)}\n\n"
        
        for i, finding in enumerate(self.expert_system.findings, 1):
            problem_data = finding['data']
            category_name = self.expert_system.ui_texts[self.current_language]["category_names"].get(finding['category'], finding['category'])
            
            if self.current_language == "en":
                report += f"{i}. Problem: {finding['problem']}\n"
                report += f"   Section: {category_name}\n"
                report += f"   Risk Level: {problem_data['risk_level']}\n"
                report += f"   Symptoms: {', '.join(problem_data['symptoms'])}\n"
                report += "   Diagnosis Steps:\n"
                for step in problem_data['diagnosis_steps']:
                    report += f"   - {step}\n"
                report += "   Suggested Solutions:\n"
                for solution in problem_data['solutions']:
                    report += f"   - {solution}\n"
                report += f"   Recommendation: {problem_data['recommendation']}\n"
            else:
                report += f"{i}. المشكلة: {finding['problem']}\n"
                report += f"   القسم: {category_name}\n"
                report += f"   مستوى الخطورة: {problem_data['risk_level']}\n"
                report += f"   الأعراض: {', '.join(problem_data['symptoms'])}\n"
                report += "   خطوات التشخيص:\n"
                for step in problem_data['diagnosis_steps']:
                    report += f"   - {step}\n"
                report += "   الحلول المقترحة:\n"
                for solution in problem_data['solutions']:
                    report += f"   - {solution}\n"
                report += f"   التوصية: {problem_data['recommendation']}\n"
            
            report += "-" * 30 + "\n"
        
        return report

    def save_report(self):
        """Save report to file"""
        report_text = self.report_text.get(1.0, tk.END)
        try:
            filename = f"car_diagnosis_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"  # FIXED
            with open(filename, "w", encoding="utf-8") as f:
                f.write(report_text)
            messagebox.showinfo("Success" if self.current_language == "en" else "نجاح", 
                            f"Report saved as {filename}" if self.current_language == "en" else f"تم حفظ التقرير باسم {filename}")
        except Exception as e:
            messagebox.showerror("Error" if self.current_language == "en" else "خطأ", 
                                f"An error occurred while saving the report: {str(e)}" if self.current_language == "en" else f"حدث خطأ أثناء حفظ التقرير: {str(e)}")
    def print_report(self):
        """Print report (simple function)"""
        messagebox.showinfo("Print" if self.current_language == "en" else "طباعة", 
                            "Report sent to printer" if self.current_language == "en" else "تم إرسال التقرير إلى الطابعة")
        
    def back_to_results(self):
        """Go back to results and clear report"""
        # Clear report content
        self.report_text.delete(1.0, tk.END)
        
        # Go back to results tab
        self.notebook.select(2)
    
    def start_new_diagnosis(self):
        """Start new diagnosis and return to welcome screen"""
        # Clear all data
        self.expert_system.findings = []
        self.expert_system.asked_questions = []
        self.question_queue = []
        self.asked_questions = set()
        self.selected_categories = []
        
        # Clear report content
        self.report_text.delete(1.0, tk.END)
        
        # Clear results
        for frame in [self.emergency_frame, self.high_risk_frame, self.medium_risk_frame, self.low_risk_frame]:
            for widget in frame.winfo_children():
                widget.destroy()
        
        # Recreate scrollable frames
        self.setup_scrollable_frame(self.emergency_frame)
        self.setup_scrollable_frame(self.high_risk_frame)
        self.setup_scrollable_frame(self.medium_risk_frame)
        self.setup_scrollable_frame(self.low_risk_frame)
        
        # Return to welcome screen
        self.notebook.select(0)
    
    def explain_reasoning(self):
        """Explain how the system reached conclusions (GUI version)"""
        if not self.expert_system.asked_questions:
            messagebox.showinfo("Information" if self.current_language == "en" else "معلومة", 
                            "No questions asked yet." if self.current_language == "en" else "لم يتم طرح أي أسئلة بعد.")
            return
        
        # Create explanation window
        explanation_window = tk.Toplevel(self.root)
        explanation_window.title(self.expert_system.ui_texts[self.current_language]["explanation_title"])
        explanation_window.geometry("900x700")
        explanation_window.configure(bg="#f0f0f0")
        
        # Window title
        title_label = tk.Label(explanation_window,
                            text=self.expert_system.ui_texts[self.current_language]["explanation_title"],
                            font=("Arial", 16, "bold"),
                            bg="#f0f0f0",
                            fg="#2c3e50")
        title_label.pack(pady=20)
        
        # Explanation text area
        explanation_text = scrolledtext.ScrolledText(explanation_window,
                                                wrap=tk.WORD,
                                                width=100,
                                                height=30,
                                                font=("Arial", 11),
                                                bg="#ffffff")
        explanation_text.pack(padx=20, pady=10, fill="both", expand=True)
        
        # Add content
        if self.current_language == "ar":
            explanation_content = "المسار المنطقي الذي اتبعته:\n"
            explanation_content += "=" * 40 + "\n\n"
        else:
            explanation_content = "Logical path followed:\n"
            explanation_content += "=" * 40 + "\n\n"
        
        for i, question_info in enumerate(self.expert_system.asked_questions, 1):
            if self.current_language == "ar":
                explanation_content += f"{i}. السؤال: {question_info['question']}\n"
                explanation_content += f"   السبب: {question_info['why_reason']}\n"
                category_name = self.expert_system.ui_texts[self.current_language]["category_names"].get(question_info['category'], question_info['category'])
                explanation_content += f"   القسم: {category_name}\n"
                explanation_content += f"   المشكلة: {question_info['problem']}\n\n"
            else:
                explanation_content += f"{i}. Question: {question_info['question']}\n"
                explanation_content += f"   Reason: {question_info['why_reason']}\n"
                category_name = self.expert_system.ui_texts[self.current_language]["category_names"].get(question_info['category'], question_info['category'])
                explanation_content += f"   Section: {category_name}\n"
                explanation_content += f"   Problem: {question_info['problem']}\n\n"
        
        explanation_text.insert(tk.END, explanation_content)
        explanation_text.config(state="disabled")  # Make text read-only
        
        # Close button
        close_button = tk.Button(explanation_window,
                            text="Close" if self.current_language == "en" else "إغلاق",
                            font=("Arial", 12),
                            bg="#e74c3c",
                            fg="white",
                            command=explanation_window.destroy,
                            padx=20,
                            pady=8)
        close_button.pack(pady=20)
    
    def show_explanation(self):
        """Show window explaining system mechanism"""
        explanation_window = tk.Toplevel(self.root)
        explanation_window.title("How the Expert System Works" if self.current_language == "en" else "كيف يعمل النظام الخبير")
        explanation_window.geometry("900x700")
        explanation_window.configure(bg="#f0f0f0")
        
        # Window title
        title_label = tk.Label(explanation_window,
                            text="How the Expert System Works" if self.current_language == "en" else "كيف يعمل النظام الخبير",
                            font=("Arial", 16, "bold"),
                            bg="#f0f0f0",
                            fg="#2c3e50")
        title_label.pack(pady=20)
        
        # Explanation text area
        explanation_text = scrolledtext.ScrolledText(explanation_window,
                                                wrap=tk.WORD,
                                                width=100,
                                                height=30,
                                                font=("Arial", 11),
                                                bg="#ffffff")
        explanation_text.pack(padx=20, pady=10, fill="both", expand=True)
        
        # Add explanation of working mechanism
        if self.current_language == "ar":
            explanation_content = """
            آلية عمل النظام الخبير لتشخيص أعطال السيارات:

            1. قاعدة المعرفة الشاملة:
            - يحتوي النظام على قاعدة معرفة ضخمة تشمل 11 قسم رئيسي لأنظمة السيارة
            - كل قسم يحتوي على عدة مشاكل محتملة مع أسئلة تشخيصية متخصصة

            2. عملية التشخيص:
            - يجمع النظام المعلومات من خلال أسئلة تفاعلية
            - يحلل الأعراض التي يقدمها المستخدم
            - يستخدم خوارزميات الذكاء الاصطناعي لتحديد المشاكل المحتملة

            3. محركات الاستدلال:
            - الاستدلال الأمامي: يبدأ من الأعراض للوصول إلى التشخيص
            - الاستدلال الخلفي: يبدأ من فرضية مشكلة ويبحث عن أدلة تؤكدها

            4. التكيف مع اللغة:
            - يدعم النظام اللغتين العربية والإنجليزية كاملًا
            - يتكيف تلقائيًا مع لغة المستخدم

            المسار التشخيصي المتبع:
            """
            
            # Add current diagnosis details
            if self.expert_system.asked_questions:
                explanation_content += "\n\nالأسئلة التي تم طرحها:\n"
                explanation_content += "=" * 30 + "\n"
                for i, question in enumerate(self.expert_system.asked_questions, 1):
                    explanation_content += f"{i}. {question['question']}\n"
            
        else:
            explanation_content = """
            How the Car Diagnostics Expert System Works:

            1. Comprehensive Knowledge Base:
            - The system contains a massive knowledge base covering 11 main car systems
            - Each section contains multiple potential problems with specialized diagnostic questions

            2. Diagnostic Process:
            - Collects information through interactive questions
            - Analyzes symptoms provided by the user
            - Uses AI algorithms to identify potential problems

            3. Inference Engines:
            - Forward Chaining: Starts from symptoms to reach diagnosis
            - Backward Chaining: Starts from hypothesis and looks for confirming evidence

            4. Language Adaptation:
            - Fully supports both Arabic and English languages
            - Automatically adapts to user's language

            Diagnostic path followed:
            """
            
            # Add current diagnosis details
            if self.expert_system.asked_questions:
                explanation_content += "\n\nQuestions asked:\n"
                explanation_content += "=" * 30 + "\n"
                for i, question in enumerate(self.expert_system.asked_questions, 1):
                    explanation_content += f"{i}. {question['question']}\n"
        
        explanation_text.insert(tk.END, explanation_content)
        explanation_text.config(state="disabled")  # Make text read-only
        
        # Control buttons
        button_frame = tk.Frame(explanation_window, bg="#f0f0f0")
        button_frame.pack(pady=20)
        
        # Show full details button
        details_button = tk.Button(button_frame,
                                text="Show Full Details" if self.current_language == "en" else "عرض التفاصيل الكاملة",
                                font=("Arial", 12),
                                bg="#3498db",
                                fg="white",
                                command=self.explain_reasoning,
                                padx=15,
                                pady=8)
        details_button.pack(side=tk.LEFT, padx=10)
        
        # Close button
        close_button = tk.Button(button_frame,
                            text="Close" if self.current_language == "en" else "إغلاق",
                            font=("Arial", 12),
                            bg="#e74c3c",
                            fg="white",
                            command=explanation_window.destroy,
                            padx=20,
                            pady=8)
        close_button.pack(side=tk.LEFT, padx=10)
    
    def exit_program(self):
        """Exit the program"""
        if messagebox.askyesno("Confirm Exit" if self.current_language == "en" else "تأكيد الخروج", 
                              "Are you sure you want to exit?" if self.current_language == "en" else "هل أنت متأكد أنك تريد الخروج؟"):
            self.root.quit()


# تشغيل التطبيق
if __name__ == "__main__":
    try:
        # Create the expert system instance
        expert_system = CarExpertSystem()
        
        # Create GUI application
        root = tk.Tk()
        app = CarExpertSystemGUI(root, expert_system)
        
        # Start the GUI event loop
        root.mainloop()
        
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        print("Please restart the program")