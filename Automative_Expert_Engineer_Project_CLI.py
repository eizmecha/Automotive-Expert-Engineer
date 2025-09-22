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
        
    def select_language(self):
        """اختيار اللغة من قبل المستخدم"""
        print("=" * 70)
        print("🌍 Please select language / الرجاء اختيار اللغة")
        print("=" * 70)
        print("1. English")
        print("2. العربية")
        print("=" * 70)
        
        while True:
            choice = input("Enter your choice (1/2): ").strip()
            if choice == "1":
                self.current_language = "en"
                break
            elif choice == "2":
                self.current_language = "ar"
                break
            else:
                print("Invalid choice. Please enter 1 for English or 2 for Arabic.")
        
        return self.current_language
    
    def select_sections(self):
        """Allow user to select specific diagnostic sections"""
        texts = self.ui_texts[self.current_language]
        
        print(f"\n{'Available Diagnostic Sections' if self.current_language == 'en' else 'أقسام التشخيص المتاحة'}:")
        print("=" * 50)
        
        categories = self.categories_map[self.current_language]
        category_names = self.ui_texts[self.current_language]["category_names"]
        
        for i, category in enumerate(categories, 1):
            print(f"{i}. {category_names.get(category, category)}")
        
        print(f"{len(categories) + 1}. {'All Sections' if self.current_language == 'en' else 'جميع الأقسام'}")
        
        prompt = f"\n{'Select sections to diagnose (comma-separated numbers)' if self.current_language == 'en' else 'اختر الأقسام للتشخيص (أرقام مفصولة بفواصل)'}: "
        
        while True:
            try:
                choices = input(prompt).split(',')
                selected_indices = [int(choice.strip()) for choice in choices]
                
                selected_categories = []
                for idx in selected_indices:
                    if 1 <= idx <= len(categories):
                        selected_categories.append(categories[idx-1])
                    elif idx == len(categories) + 1:
                        return categories  # All sections
                    else:
                        print(f"{'Invalid selection' if self.current_language == 'en' else 'اختيار غير صحيح'}: {idx}")
                
                if selected_categories:
                    return selected_categories
                else:
                    print(f"{'Please select at least one section' if self.current_language == 'en' else 'الرجاء اختيار قسم واحد على الأقل'}")
                    
            except ValueError:
                print(f"{'Please enter valid numbers' if self.current_language == 'en' else 'الرجاء إدخال أرقام صحيحة'}")
                
    def get_user_input(self, prompt, valid_options):
        """
        دالة محسنة للحصول على إدخال المستخدم مع التحقق
        """
        while True:
            try:
                user_input = input(prompt).strip().lower()
                # تحويل الإدخال بناءً على اللغة
                if self.current_language == "ar":
                    if user_input in ['نعم']:
                        user_input = 'نعم'
                    elif user_input in ['لا']:
                        user_input = 'لا'
                    elif user_input in ['لماذا']:
                        user_input = 'لماذا'
                    elif user_input in ['رجوع']:
                        user_input = 'رجوع'
                    elif user_input in ['تخطي']:
                        user_input = 'تخطي'
                    elif user_input in ['خروج']:
                        user_input = 'خروج'
                else:  # English
                    if user_input in [ 'yes']:
                        user_input = 'yes'
                    elif user_input in ['no']:
                        user_input = 'no'
                    elif user_input in [ 'why']:
                        user_input = 'why'
                    elif user_input in [ 'back']:
                        user_input = 'back'
                    elif user_input in [ 'skip']:
                        user_input = 'skip'
                    elif user_input in ['exit']:
                        user_input = 'exit'
                
                if user_input in valid_options:
                    return user_input
                else:
                    print(self.ui_texts[self.current_language]["invalid_input"].format(', '.join(valid_options)))
            except KeyboardInterrupt:
                print("\n\n" + ("Program stopped by user" if self.current_language == "en" else "تم إيقاف البرنامج بواسطة المستخدم"))
                exit()
            except Exception as e:
                print(f"{'Error occurred' if self.current_language == 'en' else 'حدث خطأ'}: {e}. {'Please try again' if self.current_language == 'en' else 'الرجاء المحاولة مرة أخرى'}")

    def display_welcome(self):
        """
        عرض شاشة الترحيب والإرشادات
        """
        texts = self.ui_texts[self.current_language]
        print("=" * 70)
        print(texts["welcome_title"])
        print("=" * 70)
        print("\n" + texts["welcome_message"])
        print("\n" + texts["instructions"])
        print("\n" + "=" * 70)

    def ask_question(self, category, problem):
        """
        طرح سؤال تشخيصي مع إدارة كاملة للتفاعل
        """
        problem_data = self.knowledge_base[self.current_language][category][problem]
        question_text = problem_data["question"]
        why_reason = problem_data["why_reason"]
        
        # تخزين معلومات السؤال للتتبع
        question_info = {
            "category": category,
            "problem": problem,
            "question": question_text,
            "why_reason": why_reason
        }
        self.asked_questions.append(question_info)
        
        # تحديد خيارات الإدخال بناءً على اللغة
        if self.current_language == "ar":
            valid_options = ['نعم', 'لا', 'لماذا', 'رجوع', 'تخطي', 'خروج']
            prompt = f"\n🔍 {question_text} (نعم/لا/لماذا/رجوع/تخطي/خروج): "
        else:
            valid_options = ['yes', 'no', 'why', 'back', 'skip', 'exit']
            prompt = f"\n🔍 {question_text} (yes/no/why/back/skip/exit): "
        
        user_answer = self.get_user_input(prompt, valid_options)
        
        # معالجة الأوامر الخاصة
        while user_answer in (['لماذا', 'why', 'رجوع', 'back', 'تخطي', 'skip', 'خروج', 'exit']):
            if user_answer in ['لماذا', 'why']:
                print(f"   ⚙️  {why_reason}")
            elif user_answer in ['رجوع', 'back']:
                # إزالة السؤال الحالي من السجل
                if len(self.asked_questions) > 1:
                    self.asked_questions.pop()  # إزالة السؤال الحالي
                    # العودة إلى السؤال السابق عن طريق تحديث المؤشرات
                    return 'back'
                else:
                    print("   " + self.ui_texts[self.current_language]["cannot_go_back"])
            elif user_answer in ['تخطي' ,'skip']:
                return 'skip'
            elif user_answer in ['خروج' ,'exit']:
                print("\n" + self.ui_texts[self.current_language]["goodbye"])
                exit()
            
            user_answer = self.get_user_input(prompt, valid_options)
        
        # تحويل الإجابة إلى قيمة boolean
        if self.current_language == "ar":
            return user_answer == "نعم"
        else:
            return user_answer == "yes"

    def diagnose_problems(self):
        """Enhanced diagnostic engine with rule relationships"""
        print("\n" + self.ui_texts[self.current_language]["start_diagnosis"] + "\n" + "=" * 60)
        
        # Let user select sections
        selected_categories = self.select_sections()
        
        # Initialize question queue with starting questions
        question_queue = []
        for category in selected_categories:
            problems = list(self.knowledge_base[self.current_language][category].keys())
            if problems:
                question_queue.append((category, problems[0]))
        
        asked_questions = set()
        current_findings = []
        
        while question_queue:
            category, problem = question_queue.pop(0)
            
            # Skip if already asked
            if (category, problem) in asked_questions:
                continue
                
            asked_questions.add((category, problem))
            
            # Display category name if it's the first question in this category
            category_name = self.ui_texts[self.current_language]["category_names"].get(category, category)
            print(f"\n{self.ui_texts[self.current_language]['checking_section'].format(category_name)}")
            print("-" * 40)
            
            # Ask the question
            result = self.ask_question(category, problem)
            
            if result == 'back':
                # Handle back navigation (you might need to adjust this)
                continue
            elif result == 'skip':
                continue
            elif result:  # User answered yes
                # Add to findings
                problem_data = self.knowledge_base[self.current_language][category][problem]
                current_findings.append({
                    'category': category,
                    'problem': problem,
                    'data': problem_data
                })
                print(f"   {self.ui_texts[self.current_language]['problem_detected'].format(problem)}")
                
                # Add dependent questions to queue
                if 'dependencies' in problem_data and 'if_yes' in problem_data['dependencies']:
                    for next_problem in problem_data['dependencies']['if_yes']:
                        # Find which category this problem belongs to
                        for cat in selected_categories:
                            if next_problem in self.knowledge_base[self.current_language][cat]:
                                question_queue.append((cat, next_problem))
                                break
            
            else:  # User answered no
                # Add alternative questions based on dependencies
                problem_data = self.knowledge_base[self.current_language][category][problem]
                if 'dependencies' in problem_data and 'if_no' in problem_data['dependencies']:
                    for next_problem in problem_data['dependencies']['if_no']:
                        # Find which category this problem belongs to
                        for cat in selected_categories:
                            if next_problem in self.knowledge_base[self.current_language][cat]:
                                question_queue.append((cat, next_problem))
                                break
        
        self.findings = current_findings
    def display_results(self):
        """
        عرض النتائج النهائية بشكل منظم
        """
        texts = self.ui_texts[self.current_language]
        
        if not self.findings:
            print("\n" + "=" * 60)
            print(texts["no_problems"])
            print("=" * 60)
            print("\n" + texts["no_problems_msg"])
            return
        
        print("\n" + "=" * 70)
        print(texts["results_title"])
        print("=" * 70)
        
        # تصنيف النتائج حسب الخطورة
        emergency_problems = []
        high_risk_problems = []
        medium_risk_problems = []
        low_risk_problems = []
        
        for finding in self.findings:
            problem_data = finding['data']
            if problem_data['emergency']:
                emergency_problems.append(finding)
            elif problem_data['risk_level'] in ['عالي', 'high']:
                high_risk_problems.append(finding)
            elif problem_data['risk_level'] in ['متوسط', 'medium']:
                medium_risk_problems.append(finding)
            else:
                low_risk_problems.append(finding)
        
        # عرض المشاكل الطارئة أولاً
        if emergency_problems:
            print("\n" + texts["emergency_problems"])
            print("=" * 50)
            for finding in emergency_problems:
                self.display_problem_details(finding, True)
        
        # عرض المشاكل عالية الخطورة
        if high_risk_problems:
            print("\n" + texts["high_risk_problems"])
            print("=" * 40)
            for finding in high_risk_problems:
                self.display_problem_details(finding)
        
        # عرض المشاكل متوسطة الخطورة
        if medium_risk_problems:
            print("\n" + texts["medium_risk_problems"])
            print("=" * 40)
            for finding in medium_risk_problems:
                self.display_problem_details(finding)
        
        # عرض المشاكل منخفضة الخطورة
        if low_risk_problems:
            print("\n" + texts["low_risk_problems"])
            print("=" * 40)
            for finding in low_risk_problems:
                self.display_problem_details(finding)

    def display_problem_details(self, finding, is_emergency=False):
        """
        عرض تفاصيل المشكلة المكتشفة
        """
        problem_data = finding['data']
        
        if is_emergency:
            print(f"\n🚨 {finding['problem'].upper()}")
        else:
            print(f"\n📌 {finding['problem']}")
        
        # عرض اسم القسم المترجم
        category_name = self.ui_texts[self.current_language]["category_names"].get(finding['category'], finding['category'])
        print(f"   📍 {('Section' if self.current_language == 'en' else 'القسم')}: {category_name}")
        print(f"   🎯 {('Symptoms' if self.current_language == 'en' else 'الأعراض')}: {', '.join(problem_data['symptoms'])}")
        print(f"   🔧 {('Diagnosis Steps' if self.current_language == 'en' else 'خطوات التشخيص')}:")
        for i, step in enumerate(problem_data['diagnosis_steps'], 1):
            print(f"      {i}. {step}")
        
        print(f"   💡 {('Suggested Solutions' if self.current_language == 'en' else 'الحلول المقترحة')}:")
        for i, solution in enumerate(problem_data['solutions'], 1):
            print(f"      {i}. {solution}")
        
        print(f"   📝 {('Recommendation' if self.current_language == 'en' else 'التوصية')}: {problem_data['recommendation']}")
        print(f"   ⚠️ {('Risk Level' if self.current_language == 'en' else 'مستوى الخطورة')}: {problem_data['risk_level']}")
        print("-" * 50)

    def explain_reasoning(self):
        """
        شرح كيفية توصل النظام إلى الاستنتاجات
        """
        if not self.asked_questions:
            print("No questions asked yet." if self.current_language == "en" else "لم يتم طرح أي أسئلة بعد.")
            return
        
        texts = self.ui_texts[self.current_language]
        print("\n" + "=" * 60)
        print(texts["explanation_title"])
        print("=" * 60)
        
        print(f"\n{'Logical path followed' if self.current_language == 'en' else 'المسار المنطقي الذي اتبعته'}:")
        print("-" * 40)
        
        for i, question_info in enumerate(self.asked_questions, 1):
            print(f"{i}. {'Question' if self.current_language == 'en' else 'السؤال'}: {question_info['question']}")
            print(f"   {'Reason' if self.current_language == 'en' else 'السبب'}: {question_info['why_reason']}")
            category_name = self.ui_texts[self.current_language]["category_names"].get(question_info['category'], question_info['category'])
            print(f"   {'Section' if self.current_language == 'en' else 'القسم'}: {category_name}")
            print(f"   {'Problem' if self.current_language == 'en' else 'المشكلة'}: {question_info['problem']}")
            print()

    def generate_report(self):
        """
        توليد تقرير مفصل عن الجلسة
        """
        if not self.findings:
            return "No problems detected." if self.current_language == "en" else "لم يتم اكتشاف أي أعطال."
        
        if self.current_language == "en":
            report = "Car Diagnostics Report\n"
            report += "=" * 40 + "\n\n"
            report += f"Diagnosis Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
            report += f"Problems Found: {len(self.findings)}\n\n"
        else:
            report = "تقرير تشخيص أعطال السيارات\n"
            report += "=" * 40 + "\n\n"
            report += f"تاريخ التشخيص: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
            report += f"عدد الأعطال المكتشفة: {len(self.findings)}\n\n"
        
        for i, finding in enumerate(self.findings, 1):
            problem_data = finding['data']
            category_name = self.ui_texts[self.current_language]["category_names"].get(finding['category'], finding['category'])
            
            if self.current_language == "en":
                report += f"{i}. Problem: {finding['problem']}\n"
                report += f"   Section: {category_name}\n"
                report += f"   Risk Level: {problem_data['risk_level']}\n"
                report += f"   Symptoms: {', '.join(problem_data['symptoms'])}\n"
                report += "   Suggested Solutions:\n"
                for solution in problem_data['solutions']:
                    report += f"   - {solution}\n"
                report += f"   Recommendation: {problem_data['recommendation']}\n"
            else:
                report += f"{i}. المشكلة: {finding['problem']}\n"
                report += f"   القسم: {category_name}\n"
                report += f"   مستوى الخطورة: {problem_data['risk_level']}\n"
                report += f"   الأعراض: {', '.join(problem_data['symptoms'])}\n"
                report += "   الحلول المقترحة:\n"
                for solution in problem_data['solutions']:
                    report += f"   - {solution}\n"
                report += f"   التوصية: {problem_data['recommendation']}\n"
            
            report += "-" * 30 + "\n"
        
        return report

    def run(self):
        """
        التشغيل الرئيسي للنظام
        """
        # اختيار اللغة أولاً
        self.select_language()
        self.display_welcome()
        
        while True:
            self.findings = []
            self.asked_questions = []
            self.current_category_index = 0
            self.current_problem_index = 0
            
            # بدء عملية التشخيص
            self.diagnose_problems()
            
            # عرض النتائج
            self.display_results()
            
            # عرض شرح الاستدلال إذا رغب المستخدم
            prompt = self.ui_texts[self.current_language]["explanation_prompt"]
            valid_options = ['yes', 'no'] if self.current_language == 'en' else ['نعم', 'لا']
            see_explanation = self.get_user_input("\n" + prompt, valid_options)
            
            if see_explanation in ['yes', 'نعم']:
                self.explain_reasoning()
            
            # عرض التقرير
            report = self.generate_report()
            print("\n" + "=" * 60)
            print(self.ui_texts[self.current_language]["report_title"])
            print("=" * 60)
            print(report)
            
            # السؤال عن جلسة جديدة
            prompt = self.ui_texts[self.current_language]["new_session_prompt"]
            valid_options = ['yes', 'no'] if self.current_language == 'en' else ['نعم', 'لا']
            new_session = self.get_user_input("\n" + prompt, valid_options)
            
            if new_session in ['no', 'لا']:
                print("\n" + self.ui_texts[self.current_language]["goodbye"])
                break

# تشغيل النظام
if __name__ == "__main__":
    try:
        expert_system = CarExpertSystem()
        expert_system.run()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        print("Please restart the program")