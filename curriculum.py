def get_curriculum(level, subject_id):
    level_lower = level.lower()
    
    # ------------------
    # MATERNELLE (الروض)
    # ------------------
    if "الروض" in level_lower:
        return {
            "semester_1": [
                "Thème 1 : Mon école et mes amis",
                "Thème 2 : Mon corps et ma santé",
                "Thème 3 : Ma famille et mon foyer"
            ],
            "semester_2": [
                "Thème 4 : Le monde de la nature (Plantes et animaux)",
                "Thème 5 : L'eau, source de vie",
                "Thème 6 : Les jeux et l'espace créatif"
            ]
        }

    # ------------------
    # PRIMAIRE (ابتدائي)
    # ------------------
    if "ابتدائي" in level_lower:
        if subject_id == "math":
            return {
                "semester_1": ["Les nombres", "Addition et soustraction", "La géométrie de base", "La mesure de longueurs"],
                "semester_2": ["Multiplication (et division pour les grands)", "Les fractions", "Les figures géométriques", "Résolution de problèmes"]
            }
        elif subject_id == "french":
            return {
                "semester_1": ["Unité 1 : Le monde des amis", "Unité 2 : La vie scolaire", "Unité 3 : La famille"],
                "semester_2": ["Unité 4 : L'environnement", "Unité 5 : La santé et la maladie", "Unité 6 : Les voyages"]
            }
        elif subject_id == "arabic":
            return {
                "semester_1": ["مجال العائلة", "مجال المدرسة", "مجال التغذية والصحة"],
                "semester_2": ["مجال القرية والمدينة", "مجال البيئة", "مجال الرحلات والأسفار"]
            }
        elif subject_id == "science":
            return {
                "semester_1": ["Les sens et la santé", "L'alimentation", "Le mouvement"],
                "semester_2": ["L'eau et la nature", "L'électricité simple", "Les plantes et les animaux"]
            }
        elif subject_id == "islamic":
            return {
                "semester_1": ["Coran : Sourates courtes", "Dogme : Croire en Dieu", "Culte : Les ablutions"],
                "semester_2": ["Coran : Récitation et compréhension", "Biographie du Prophète (Sira)", "Morale et bon comportement"]
            }
        else:
            return {
                "semester_1": ["Semestre 1 - Unité 1", "Semestre 1 - Unité 2", "Semestre 1 - Unité 3"],
                "semester_2": ["Semestre 2 - Unité 4", "Semestre 2 - Unité 5", "Semestre 2 - Unité 6"]
            }

    # ------------------
    # COLLÈGE (إعدادي)
    # ------------------
    if "إعدادي" in level_lower:
        if "الأولى" in level_lower or "1" in level_lower:
            if subject_id == "svt":
                return {
                    "semester_1": ["Exploration des milieux naturels", "La respiration dans différents milieux", "L'alimentation chez les êtres vivants"],
                    "semester_2": ["Les relations trophiques dans un milieu naturel", "La géologie externe : formation des roches sédimentaires", "L'échelle stratigraphique"]
                }
            elif subject_id == "physics":
                return {
                    "semester_1": ["L'eau dans notre environnement", "Les trois états de la matière", "Le modèle particulaire de la matière", "La masse et le volume"],
                    "semester_2": ["L'électricité autour de nous", "Le circuit électrique simple", "Les conducteurs et les isolants", "Montage en série et en parallèle"]
                }
            elif subject_id == "math":
                return {
                    "semester_1": ["Les nombres entiers naturels et décimaux", "Les nombres fractionnaires", "La géométrie de base : droites et segments"],
                    "semester_2": ["Les nombres relatifs (Addition et soustraction)", "Les angles", "Les triangles", "La symétrie centrale"]
                }
        elif "الثانية" in level_lower or "2" in level_lower:
            if subject_id == "svt":
                return {
                    "semester_1": ["La géologie interne : Les séismes et la structure du globe", "Le volcanisme et les roches magmatiques", "La tectonique des plaques"],
                    "semester_2": ["La reproduction sexuée chez les animaux", "La reproduction sexuée chez les végétaux", "La reproduction chez l'Homme et la santé"]
                }
            elif subject_id == "physics":
                return {
                    "semester_1": ["L'air qui nous entoure", "Propriétés de l'air", "Les molécules et les atomes", "La réaction chimique"],
                    "semester_2": ["La lumière : sources et récepteurs", "La propagation rectiligne de la lumière", "Les lentilles minces", "L'étude de l'œil"]
                }
        elif "الثالثة" in level_lower or "3" in level_lower:
            if subject_id == "svt":
                return {
                    "semester_1": ["La digestion et l'absorption intestinale", "La respiration", "Le sang et la circulation sanguine", "L'excrétion urinaire"],
                    "semester_2": ["Le système nerveux", "Le système musculaire", "Le système immunitaire", "Les dysfonctionnements du système immunitaire"]
                }
            elif subject_id == "physics":
                return {
                    "semester_1": ["Exemples de quelques matériaux", "Les atomes et les ions", "Action des solutions acides et basiques", "Tests de reconnaissance de quelques ions"],
                    "semester_2": ["Le mouvement et le repos", "La vitesse", "Les actions mécaniques", "Le poids et la masse", "La loi d'Ohm"]
                }
            elif subject_id == "math":
                return {
                    "semester_1": ["Identités remarquables et puissances", "Théorème de Thalès", "Théorème de Pythagore", "Trigonométrie"],
                    "semester_2": ["Les équations et inéquations", "Vecteurs et translation", "Repère dans le plan", "Équation d'une droite", "Systèmes d'équations"]
                }
                
    # ------------------
    # LYCÉE QUALIFIANT (جذع مشترك, 1 باك, 2 باك)
    # ------------------
    subject_map = {
        "math": "Mathématiques",
        "physics": "Physique-Chimie",
        "svt": "Sciences de la Vie et de la Terre (SVT)",
        "french": "Français",
        "english": "Anglais",
        "philosophy": "Philosophie",
        "history_geo": "Histoire et Géographie",
        "islamic": "Éducation Islamique",
        "arabic": "Langue Arabe",
        "informatique": "Informatique",
        "pe": "Éducation Physique"
    }
    
    LYCEE_QUALIFIANT_CURRICULUM = {
        "Tronc Commun": {
            "Mathématiques": {
                "semester_1": [
                    "Notions de logique et terminologie mathématique",
                    "Généralités sur les fonctions numériques (Variations, extrema)",
                    "Le produit scalaire dans le plan et applications",
                    "Les suites numériques (Généralités et modes de génération)"
                ],
                "semester_2": [
                    "La trigonométrie (Cercle trigonométrique, angles et équations)",
                    "Géométrie analytique dans l'espace (Repérage, droites et plans)",
                    "La dérivation et applications (Taux d'accroissement, tangente)",
                    "Statistiques (Séries à caractère continu) et Probabilités"
                ]
            },
            "Physique-Chimie": {
                "semester_1": [
                    "Le mouvement et la gravitation universelle (Lois de Kepler)",
                    "Les interactions mécaniques et les lois de Newton",
                    "Les espèces chimiques, la mole et la concentration molaire",
                    "Les solutions aqueuses et la conductibilité électrique"
                ],
                "semester_2": [
                    "L'électricité : Courant continu, tension et lois des circuits",
                    "Les transformations de la matière en chimie (Oxydoréduction)",
                    "L'optique géométrique (Lentilles minces et images)",
                    "Le spectre lumineux et les ondes électromagnétiques simples"
                ]
            },
            "Sciences de la Vie et de la Terre (SVT)": {
                "semester_1": [
                    "L'écologie : Étude des écosystèmes naturels et facteurs abiotiques",
                    "La géodynamique externe et l'histoire géologique de la Terre",
                    "La sédimentation et la formation des bassins sédimentaires"
                ],
                "semester_2": [
                    "La reproduction sexuée et asexuée chez les plantes et les animaux",
                    "L'hérédité biologique et la transmission des caractères chez les êtres vivants",
                    "La gestion et la protection rationnelle des ressources naturelles"
                ]
            },
            "Français": {
                "semester_1": [
                    "Module 1 : La nouvelle réaliste (Étude des structures narratives et thématiques)",
                    "Module 2 : La poésie (Formes poétiques, versification et figures de style)"
                ],
                "semester_2": [
                    "Module 3 : Le théâtre (Analyse dramaturgique et textes argumentatifs)",
                    "Module 4 : La nouvelle fantastique ou policière"
                ]
            },
            "Anglais": {
                "semester_1": [
                    "Unit 1 : Getting Started and Personal Information",
                    "Unit 2 : Education and Youth Aspirations",
                    "Unit 3 : Humor, Wit and Entertainment"
                ],
                "semester_2": [
                    "Unit 4 : Women and Society",
                    "Unit 5 : Science, Technology and Progress",
                    "Unit 6 : Sustainable Development and Environment"
                ]
            },
            "Philosophie": {
                "semester_1": [
                    "Séquence 1 : Introduction générale à la réflexion philosophique et mythe",
                    "Séquence 2 : La nature humaine (L'homme entre culture et nature)"
                ],
                "semester_2": [
                    "Séquence 3 : La société (Les liens sociaux, l'échange et la violence)",
                    "Séquence 4 : L'art, la liberté et l'existence humaine"
                ]
            },
            "Histoire et Géographie": {
                "semester_1": [
                    "Histoire 1 : Les transformations du monde occidental (XVe - XVIIIe siècle)",
                    "Histoire 2 : Le capitalisme européen et l'essor de la bourgeoisie",
                    "Géographie 1 : L'environnement géographique mondial et cartographie"
                ],
                "semester_2": [
                    "Histoire 3 : L'Europe et le monde au XIXe siècle",
                    "Géographie 2 : Les dynamiques de la population mondiale et urbanisation",
                    "Géographie 3 : Le développement durable et les grands déséquilibres"
                ]
            },
            "Éducation Islamique": {
                "semester_1": [
                    "Unité 1 : التزكية (توحيد الله وخصائص العقيدة الإسلامية)",
                    "Unité 2 : الاقتداء (نموذج الرسول صلى الله عليه وسلم في الدعوة والصبر)"
                ],
                "semester_2": [
                    "Unité 3 : الاستجابة والقسط (مقاصد الشريعة، حقوق الإنسان والطفل)",
                    "Unité 4 : الحكمة (التعايش، التسامح وحوار الحضارات في الإسلام)"
                ]
            },
            "Langue Arabe": {
                "semester_1": [
                    "الوحدة 1 : قضايا معاصرة (البيئة، التواصل، قضايا الشباب)",
                    "الوحدة 2 : الدرس اللغوي (المجرد والمزيد، المصادر، الممنوع من الصرف)"
                ],
                "semester_2": [
                    "الوحدة 3 : إبداعات أدبية وفنية عالمية ومحلية",
                    "الوحدة 4 : التعبير والإنشاء (فن التخيل، كتابة سيرة ذاتية أو غيرية)"
                ]
            },
            "Informatique": {
                "semester_1": ["Unit 1 : Systèmes informatiques et architecture matérielle", "Unit 2 : Traitement de données et outils bureautiques avancés"],
                "semester_2": ["Unit 3 : Algorithmique et programmation (Python / Scratch)", "Unit 4 : Sécurité informatique, réseaux et éthique numérique"]
            }
        },
        "1ère Bac": {
            "Mathématiques": {
                "semester_1": [
                    "Unité 1 : La dérivation (Calculs, tangentes et étude des variations)",
                    "Unité 2 : Les suites arithmétiques et géométriques",
                    "Unité 3 : La trigonométrie (Transformations, équations et inéquations)",
                    "Unité 4 : Le produit scalaire dans le plan et ses applications analytiques"
                ],
                "semester_2": [
                    "Unité 5 : Le calcul des limites et la continuité d'une fonction",
                    "Unité 6 : Les transformations du plan (Homothéties et rotations)",
                    "Unité 7 : La géométrie dans l'espace (Droites, plans et orthogonalité)",
                    "Unité 8 : Le dénombrement et le calcul des probabilités"
                ]
            },
            "Physique-Chimie": {
                "semester_1": [
                    "Unité 1 : Le travail et l'énergie mécanique (Théorème de l'énergie cinétique)",
                    "Unité 2 : L'énergie thermique et les transferts thermiques",
                    "Unité 3 : Le champ magnétique et le courant alternatif sinusoïdal",
                    "Unité 4 : L'optique géométrique (Instruments d'optique : loupe, lunette)"
                ],
                "semester_2": [
                    "Unité 5 : La chimie organique (Généralités, hydrocarbures et fonctions oxygénées)",
                    "Unité 6 : La vitesse d'une réaction chimique et facteurs cinétiques",
                    "Unité 7 : Les lois de l'électrocinétique (Dipôles RC et RLC en régime transitoire)"
                ]
            },
            "Sciences de la Vie et de la Terre (SVT)": {
                "semester_1": [
                    "Unité 1 : La tectonique des plaques et l'histoire géologique de la Terre",
                    "Unité 2 : Le magmatisme et son rôle dans la tectonique des plaques",
                    "Unité 3 : La déformation tectonique (Plis, failles, nappes de charriage)"
                ],
                "semester_2": [
                    "Unité 4 : La communication nerveuse et la communication hormonale",
                    "Unité 5 : L'immunologie et les mécanismes de défense de l'organisme",
                    "Unité 6 : Les dysfonctionnements du système immunitaire (SIDA, allergies)"
                ]
            },
            "Français": {
                "semester_1": [
                    "Séquence 1 : Étude de l'œuvre intégrale 'La Boîte à Merveilles' d'Ahmed Sefrioui",
                    "Séquence 2 : Étude de l'œuvre théâtrale 'Antigone' de Jean Anouilh"
                ],
                "semester_2": [
                    "Séquence 3 : Étude de l'œuvre argumentative 'Le Dernier Jour d'un Condamné' de Victor Hugo",
                    "Séquence 4 : Méthodologie de la production écrite et préparation à l'Examen Régional"
                ]
            },
            "Anglais": {
                "semester_1": [
                    "Unit 1 : Education and Formal / Non-formal Learning",
                    "Unit 2 : Gifts of Youth, Leadership and Civic Action",
                    "Unit 3 : Humor, Wit and Psychological Well-being"
                ],
                "semester_2": [
                    "Unit 4 : Women's Empowerment and Societal Role",
                    "Unit 5 : Advances in Science and Technology",
                    "Unit 6 : Sustainable Development, Environment and Ecology"
                ]
            },
            "Philosophie": {
                "semester_1": [
                    "Champ 1 : La Condition Humaine (La personne, l'autonomie et la liberté)",
                    "Champ 2 : La Connaissance (La science, la théorie et la vérité)"
                ],
                "semester_2": [
                    "Champ 3 : La Politique (L'État, la violence, le droit et la justice)",
                    "Champ 4 : La Morale (Le devoir, le bonheur et la conscience morale)"
                ]
            },
            "Histoire et Géographie": {
                "semester_1": [
                    "Histoire 1 : L'impérialisme occidental à la fin du XIXe et début XXe siècle",
                    "Histoire 2 : La Première Guerre mondiale (1914-1918) : Bilan et mutations",
                    "Géographie 1 : Les grandes puissances mondiales (États-Unis, Chine, UE)"
                ],
                "semester_2": [
                    "Histoire 3 : La crise économique mondiale de 1929 et ses répercussions",
                    "Histoire 4 : La Seconde Guerre mondiale (1939-1945) et les relations internationales",
                    "Géographie 2 : Le sous-développement et la mondialisation (Défis et enjeux)"
                ]
            },
            "Éducation Islamique": {
                "semester_1": [
                    "Unité 1 : العقيدة وقضايا الفكر والفلسفة الإيمانية",
                    "Unité 2 : الاقتداء (نماذج السيرة في بناء الدولة والثبات على المبدأ)"
                ],
                "semester_2": [
                    "Unité 3 : الاستجابة والقسط (أحكام الأسرة، حقوق المرأة والطفل)",
                    "Unité 4 : الحكمة (القيم الحقوقية، السلم والتعايش الكوني)"
                ]
            },
            "Langue Arabe": {
                "semester_1": [
                    "الوحدة 1 : قضايا أدبية وفكرية معاصرة في الشعر والنثر",
                    "الوحدة 2 : الدرس البلاغي والعروضي (علوم البيان، البديع وبحور الشعر العربي)"
                ],
                "semester_2": [
                    "الوحدة 3 : التيارات النقدية والأدبية الحديثة",
                    "الوحدة 4 : مهارة تحليل النصوص والقولات الأدبية والنقدية"
                ]
            },
            "Éducation Physique": {
                "semester_1": ["Unit 1 : Sports collectifs de performance (Football / Basketball)", "Unit 2 : Gymnastique sportive et au sol"],
                "semester_2": ["Unit 3 : Athlétisme (Saut en longueur, lancer du poids)", "Unit 4 : Course de demi-fond et endurances"]
            }
        },
        "2ème Bac": {
            "Mathématiques": {
                "semester_1": [
                    "Unité 1 : Les limites et la continuité des fonctions numériques",
                    "Unité 2 : La dérivabilité et l'étude complète des fonctions",
                    "Unité 3 : Les suites numériques (Convergences et théorèmes de convergence)",
                    "Unité 4 : Les fonctions logarithmiques (Ln) et exponentielles (Exp)"
                ],
                "semester_2": [
                    "Unité 5 : Les nombres complexes (Formes algébrique, trigonométrique et géométrie)",
                    "Unité 6 : Le calcul intégral (Primitives, intégrales et applications aux aires/volumes)",
                    "Unité 7 : Les équations différentielles du premier et second ordre",
                    "Unité 8 : Géométrie dans l'espace (Produit vectoriel) et Probabilités conditionnelles"
                ]
            },
            "Physique-Chimie": {
                "semester_1": [
                    "Unité 1 : Les ondes mécaniques progressives et périodiques",
                    "Unité 2 : La propagation des ondes lumineuses (Interférences et diffraction)",
                    "Unité 3 : La désintégration radioactive et l'énergie nucléaire (Noyaux et masse)",
                    "Unité 4 : L'électricité : Dipôles RC, RLC et Oscillations libres dans un circuit RLC",
                    "Unité 5 : Les transformations lentes et rapides d'un système chimique"
                ],
                "semester_2": [
                    "Unité 6 : Le suivi temporel d'une réaction chimique et la vitesse de réaction",
                    "Unité 7 : L'état d'équilibre d'un système chimique (Acides et bases, pH)",
                    "Unité 8 : La mécanique de Newton (Chutes libres, plans inclinés et mouvements plans)",
                    "Unité 9 : Les systèmes oscillants mécaniques et l'énergétique",
                    "Unité 10 : La modulation d'amplitude et les ondes électromagnétiques de télécommunication"
                ]
            },
            "Sciences de la Vie et de la Terre (SVT)": {
                "semester_1": [
                    "Unité 1 : L'information génétique et sa transmission par la reproduction sexuée (Méiose et fécondation)",
                    "Unité 2 : Les lois statistiques de la transmission des caractères héréditaires (Génétique mendélienne)",
                    "Unité 3 : La génétique humaine (Arbres généalogiques, caryotypes et anomalies)",
                    "Unité 4 : Le génie génétique et ses applications biotechnologiques"
                ],
                "semester_2": [
                    "Unité 5 : L'immunologie (Défense immunitaire innée et acquise, sérothérapie et vaccination)",
                    "Unité 6 : Le transfert d'énergie musculaire (Contraction musculaire et métabolisme énergétique)",
                    "Unité 7 : La géologie : Phénomènes géologiques accompagnant la formation des chaînes de montagnes"
                ]
            },
            "Français": {
                "semester_1": [
                    "Module 1 : Étude du conte philosophique 'Candide ou l'Optimisme' de Voltaire",
                    "Module 2 : Étude du drame romantique 'On ne badine pas avec l'amour' d'Alfred de Musset"
                ],
                "semester_2": [
                    "Module 3 : Étude du roman réaliste 'Le Père Goriot' d'Honoré de Balzac",
                    "Module 4 : Stratégies de synthèse et préparation intensive à l'Examen National"
                ]
            },
            "Anglais": {
                "semester_1": [
                    "Unit 1 : Cultural Issues and Values in a Globalized World",
                    "Unit 2 : Gifts of Youth, Civic Engagement and Volunteering",
                    "Unit 3 : Women and Power in Contemporary Societies"
                ],
                "semester_2": [
                    "Unit 4 : Advances in Science and Technology (AI, Bioethics)",
                    "Unit 5 : Sustainable Development, Renewable Energy and Ecology",
                    "Unit 6 : International Organizations, Human Rights and Global Citizenship"
                ]
            },
            "Philosophie": {
                "semester_1": [
                    "المجزوءة الأولى: الوضع البشري (مفهوم الشخص، مفهوم الغير، مفهوم التاريخ)",
                    "المجزوءة الثانية: المعرفة (التجربة والتجربة، النظرية والتوبريت، الحقيقة)"
                ],
                "semester_2": [
                    "المجزوءة الثالثة: السياسة (مفهوم الدولة، مفهوم الحق والعدالة)",
                    "المجزوءة الرابعة: الأخلاق (مفهوم الواجب، مفهوم السعادة، مفهوم الحرية)"
                ]
            },
            "Histoire et Géographie": {
                "semester_1": [
                    "Histoire 1 : Le système mondial bipolaire (Guerre froide) et la multipolarité",
                    "Histoire 2 : Les transformations politiques et géo-économiques mondiales après 1989",
                    "Géographie 1 : Les grandes puissances et pays émergents (États-Unis, Chine, UE, Brésil, Inde)"
                ],
                "semester_2": [
                    "Histoire 3 : Le monde arabe : Les défis du développement régional et de la décolonisation",
                    "Géographie 2 : L'Union Européenne et les blocs économiques régionaux dans l'économie globale",
                    "Géographie 3 : Bilan global et révisions intensives pour l'Examen National"
                ]
            },
            "Éducation Islamique": {
                "semester_1": [
                    "Unité 1 : التزكية (الإيمان والغيب، فلسفة الوجود والكون)",
                    "Unité 2 : الاقتداء (الرسول صلى الله عليه وسلم في بيئة الرسالة والبناء المجتمعي)"
                ],
                "semester_2": [
                    "Unité 3 : الاستجابة والقسط (الأسرة، حقوق الإنسان، المعاملات المالية والاقتصادية)",
                    "Unité 4 : الحكمة (قيم السلم، التعايش، وحماية البيئة الكونية)"
                ]
            },
            "Langue Arabe": {
                "semester_1": [
                    "الوحدة 1 : قضايا تجديد الأدب العربي الحديث (شعر إحيائها، القصة، المسرحية)",
                    "الوحدة 2 : مناهج النقد الأدبي الحديث (المنهج الاجتماعي والبنيوي)"
                ],
                "semester_2": [
                    "الوحدة 3 : قضايا الفكر العربي المعاصر (الأصالة والمعاصرة، التنمية)",
                    "الوحدة 4 : التحضير الشامل والنهائي للامتحان الوطني للبكالوريا"
                ]
            },
            "Éducation Physique": {
                "semester_1": ["Unit 1 : Sports collectifs d'élite (Football / Volleyball)", "Unit 2 : Performance gymnique et équilibre"],
                "semester_2": ["Unit 3 : Athlétisme de compétition (Course de haies et demi-fond)", "Unit 4 : Évaluation finale et tests d'endurance"]
            }
        }
    }
    
    if subject_id in subject_map:
        subject_name_key = subject_map[subject_id]
        lycee_level_key = None
        if "جذع مشترك" in level_lower:
            lycee_level_key = "Tronc Commun"
        elif "1 باك" in level_lower:
            lycee_level_key = "1ère Bac"
        elif "2 باك" in level_lower:
            lycee_level_key = "2ème Bac"
            
        if lycee_level_key and subject_name_key in LYCEE_QUALIFIANT_CURRICULUM[lycee_level_key]:
            curriculum_data = LYCEE_QUALIFIANT_CURRICULUM[lycee_level_key][subject_name_key]
            # Convert Semester 1 and Semester 2 keys to semester_1 and semester_2
            return {
                "semester_1": curriculum_data.get("Semestre 1", curriculum_data.get("semester_1", [])),
                "semester_2": curriculum_data.get("Semestre 2", curriculum_data.get("semester_2", []))
            }

    # Default fallback for any unmapped subject/level
    return {
        "semester_1": ["Unité 1 : Introduction et Fondamentaux", "Unité 2 : Concepts de base", "Unité 3 : Applications pratiques"],
        "semester_2": ["Unité 4 : Théories avancées", "Unité 5 : Études de cas", "Unité 6 : Synthèse et révision"]
    }
