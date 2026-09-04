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
    # LYCÉE (جذع مشترك, 1 باك, 2 باك)
    # ------------------
    if "جذع مشترك" in level_lower:
        if subject_id == "svt":
            return {
                "semester_1": ["L'écologie : Sortie écologique", "Les facteurs édaphiques", "Les facteurs climatiques", "Le flux d'énergie et de la matière"],
                "semester_2": ["La reproduction sexuée chez les plantes sans fleurs", "La reproduction sexuée chez les plantes à fleurs", "La modification génétique"]
            }
        elif subject_id == "physics":
            return {
                "semester_1": ["La gravitation universelle", "Le mouvement", "Principe d'inertie", "La quantité de matière (La mole)"],
                "semester_2": ["Le courant électrique continu", "La tension électrique", "L'extraction et la synthèse des espèces chimiques"]
            }
        elif subject_id == "math":
            return {
                "semester_1": ["L'arithmétique dans IN", "Le calcul vectoriel", "La projection", "L'ordre dans IR"],
                "semester_2": ["Les polynômes", "Les équations, inéquations et systèmes", "Les fonctions numériques", "La géométrie dans l'espace"]
            }
            
    elif "1 باك" in level_lower:
        if subject_id == "svt":
            return {
                "semester_1": ["La réalisation de la carte paléogéographique d'une région donnée", "Les principes de la stratigraphie", "La carte géologique"],
                "semester_2": ["Les mécanismes d'absorption de l'eau et des sels minéraux chez les plantes", "Les échanges gazeux chlorophylliens", "La production de la matière organique (Photosynthèse)", "La communication hormonale (La glycémie)"]
            }
        elif subject_id == "physics":
            return {
                "semester_1": ["Le mouvement de rotation d'un corps solide", "Le travail et la puissance mécanique", "Le travail et l'énergie cinétique", "La mesure en chimie"],
                "semester_2": ["L'énergie potentielle de pesanteur", "L'énergie mécanique", "Les dosages acido-basiques", "Le champ magnétique"]
            }
        elif subject_id == "math":
            return {
                "semester_1": ["La logique mathématique", "Généralités sur les fonctions", "Le barycentre", "Les suites numériques"],
                "semester_2": ["Le calcul trigonométrique", "La dérivation", "L'étude de fonctions", "La géométrie dans l'espace"]
            }
        elif subject_id == "arabic":
            return {
                "semester_1": ["المجزوءة الأولى: أنواع الخطاب (الإشهاري، الصحفي، السياسي)", "المجزوءة الثانية: قضايا معاصرة (الإنسان والتنمية، التكنولوجيا)"],
                "semester_2": ["المجزوءة الثالثة: المفاهيم (الحداثة، التواصل، الإبداع)", "المجزوءة الرابعة: القيم (التضامن، التسامح، الجمال)"]
            }

    elif "2 باك" in level_lower:
        if subject_id == "svt":
            return {
                "semester_1": ["La consommation de la matière organique et le flux d'énergie", "Nature et mécanisme de l'expression du matériel génétique (ADN)", "La transmission de l'information génétique lors de la reproduction sexuée", "Les lois statistiques de la transmission des caractères héréditaires"],
                "semester_2": ["L'utilisation des matières organiques et inorganiques (Pollution)", "Les phénomènes géologiques accompagnant la formation des chaînes de montagnes", "Le métamorphisme et la granitisation"]
            }
        elif subject_id == "physics":
            return {
                "semester_1": ["Les ondes mécaniques progressives", "Les ondes lumineuses", "Transformations nucléaires : Décroissance radioactive", "Suivi temporel d'une transformation chimique"],
                "semester_2": ["Les circuits RC, RL et RLC en série", "La mécanique : Lois de Newton", "La chute verticale", "Le mouvement des projectiles", "Les réactions d'estérification et d'hydrolyse"]
            }
        elif subject_id == "math":
            return {
                "semester_1": ["Limites et continuité", "La dérivabilité et l'étude des fonctions", "Les suites numériques", "Les fonctions logarithmiques"],
                "semester_2": ["Les nombres complexes", "Les fonctions exponentielles", "Le calcul intégral", "Les équations différentielles", "La géométrie dans l'espace", "Le calcul des probabilités"]
            }
        elif subject_id == "philosophy":
            return {
                "semester_1": ["La condition humaine : La Personne", "La condition humaine : Autrui", "La condition humaine : L'Histoire"],
                "semester_2": ["La connaissance : La théorie et l'expérience", "La connaissance : La vérité", "La politique : L'État", "La morale : Le devoir, la liberté"]
            }

    # Default fallback for any unmapped subject/level
    return {
        "semester_1": ["Unité 1 : Introduction et Fondamentaux", "Unité 2 : Concepts de base", "Unité 3 : Applications pratiques"],
        "semester_2": ["Unité 4 : Théories avancées", "Unité 5 : Études de cas", "Unité 6 : Synthèse et révision"]
    }
