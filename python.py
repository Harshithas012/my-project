from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


# =========================================================
# EXERCISES
# =========================================================

EXERCISES = {

    "Neck Stretch": {
        "type": "neck",
        "min": 20,
        "max": 45,
        "good": "Good! Hold the position.",
        "low": "Raise your head slightly."
    },

    "Neck Rotation": {
        "type": "neck",
        "min": 30,
        "max": 60,
        "good": "Good neck rotation!",
        "low": "Turn your head a little more."
    },

    "Chin Tuck": {
        "type": "neck",
        "min": 30,
        "max": 60,
        "good": "Good! Keep your chin position.",
        "low": "Move your chin slightly."
    },

    "Shoulder Stretch": {
        "type": "arm",
        "min": 50,
        "max": 100,
        "good": "Good shoulder position!",
        "low": "Raise your arm more."
    },

    "Shoulder Rotation": {
        "type": "arm",
        "min": 60,
        "max": 120,
        "good": "Good shoulder movement!",
        "low": "Move your arm a little more."
    },

    "Arm Raise Exercise": {
        "type": "arm",
        "min": 70,
        "max": 130,
        "good": "Good! Hold your arm.",
        "low": "Raise your arm more."
    },

    "Arm Stretch": {
        "type": "arm",
        "min": 60,
        "max": 120,
        "good": "Good arm stretch!",
        "low": "Stretch your arm a little more."
    },

    "Arm Circles": {
        "type": "arm",
        "min": 50,
        "max": 120,
        "good": "Good arm movement!",
        "low": "Move your arm a little more."
    },

    "Wrist Rotation": {
        "type": "arm",
        "min": 40,
        "max": 100,
        "good": "Good wrist movement!",
        "low": "Rotate your wrist a little more."
    },

    "Wrist Flexion": {
        "type": "arm",
        "min": 30,
        "max": 90,
        "good": "Good wrist position!",
        "low": "Move your wrist more."
    },

    "Wrist Extension": {
        "type": "arm",
        "min": 30,
        "max": 90,
        "good": "Good wrist extension!",
        "low": "Extend your wrist more."
    },

    "Finger Stretch": {
        "type": "arm",
        "min": 20,
        "max": 80,
        "good": "Good finger movement!",
        "low": "Open your fingers more."
    },

    "Hand Open and Close": {
        "type": "arm",
        "min": 20,
        "max": 90,
        "good": "Good hand movement!",
        "low": "Open and close your hand more."
    },

    "Knee Extension": {
        "type": "knee",
        "min": 70,
        "max": 160,
        "good": "Good knee position!",
        "low": "Extend your knee more."
    },

    "Knee Bend Exercise": {
        "type": "knee",
        "min": 60,
        "max": 130,
        "good": "Good knee bend!",
        "low": "Bend your knee a little more."
    },

    "Straight Leg Raise": {
        "type": "leg",
        "min": 50,
        "max": 100,
        "good": "Good leg position!",
        "low": "Raise your leg more."
    },

    "Seated Leg Raise": {
        "type": "leg",
        "min": 60,
        "max": 120,
        "good": "Good seated leg movement!",
        "low": "Raise your leg more."
    },

    "Seated Knee Extension": {
        "type": "knee",
        "min": 70,
        "max": 160,
        "good": "Good knee extension!",
        "low": "Extend your knee more."
    },

    "Mini Squat": {
        "type": "knee",
        "min": 70,
        "max": 130,
        "good": "Good squat position!",
        "low": "Bend your knees slightly more."
    },

    "Hip Rotation": {
        "type": "hip",
        "min": 40,
        "max": 100,
        "good": "Good hip movement!",
        "low": "Move your hip a little more."
    },

    "Hip Stretch": {
        "type": "hip",
        "min": 50,
        "max": 110,
        "good": "Good hip stretch!",
        "low": "Stretch your hip a little more."
    },

    "Hip Abduction": {
        "type": "hip",
        "min": 40,
        "max": 100,
        "good": "Good hip position!",
        "low": "Move your leg outward more."
    },

    "Standing Leg Raise": {
        "type": "leg",
        "min": 40,
        "max": 100,
        "good": "Good leg raise!",
        "low": "Raise your leg more."
    },

    "Ankle Rotation": {
        "type": "leg",
        "min": 20,
        "max": 80,
        "good": "Good ankle movement!",
        "low": "Rotate your ankle more."
    },

    "Ankle Flexion": {
        "type": "leg",
        "min": 20,
        "max": 80,
        "good": "Good ankle position!",
        "low": "Move your ankle more."
    },

    "Heel Raise": {
        "type": "leg",
        "min": 30,
        "max": 100,
        "good": "Good heel raise!",
        "low": "Raise your heels more."
    },

    "Toe Raise": {
        "type": "leg",
        "min": 20,
        "max": 80,
        "good": "Good toe movement!",
        "low": "Raise your toes more."
    },

    "Calf Stretch": {
        "type": "leg",
        "min": 40,
        "max": 100,
        "good": "Good calf stretch!",
        "low": "Stretch your calf a little more."
    },

    "Upper Back Stretch": {
        "type": "back",
        "min": 30,
        "max": 90,
        "good": "Good upper back stretch!",
        "low": "Stretch a little more."
    },

    "Lower Back Stretch": {
        "type": "back",
        "min": 30,
        "max": 90,
        "good": "Good lower back position!",
        "low": "Move a little more carefully."
    },

    "Side Bend": {
        "type": "side",
        "min": 30,
        "max": 80,
        "good": "Good side bend!",
        "low": "Bend slightly more."
    },

    "Balance Stand": {
        "type": "balance",
        "min": 20,
        "max": 80,
        "good": "Good balance! Hold the position.",
        "low": "Try to maintain your position."
    },

    "Marching in Place": {
        "type": "leg",
        "min": 40,
        "max": 100,
        "good": "Good marching movement!",
        "low": "Lift your knee a little more."
    },

    "Gentle Full-Body Stretch": {
        "type": "fullbody",
        "min": 30,
        "max": 100,
        "good": "Good full-body movement!",
        "low": "Stretch a little more."
    }
}


# =========================================================
# CONDITION → EXERCISES
# =========================================================

CONDITION_EXERCISES = {

    "elderly": [
        "Seated Leg Raise",
        "Shoulder Stretch",
        "Neck Stretch",
        "Balance Stand",
        "Marching in Place"
    ],

    "general": [
        "Gentle Full-Body Stretch",
        "Shoulder Stretch",
        "Neck Stretch",
        "Marching in Place"
    ],

    "knee": [
        "Knee Extension",
        "Knee Bend Exercise",
        "Seated Knee Extension",
        "Straight Leg Raise",
        "Mini Squat"
    ],

    "shoulder": [
        "Shoulder Stretch",
        "Shoulder Rotation",
        "Arm Raise Exercise",
        "Arm Stretch",
        "Arm Circles"
    ],

    "wrist": [
        "Wrist Rotation",
        "Wrist Flexion",
        "Wrist Extension"
    ],

    "hand": [
        "Finger Stretch",
        "Hand Open and Close",
        "Wrist Rotation"
    ],

    "ankle": [
        "Ankle Rotation",
        "Ankle Flexion",
        "Heel Raise",
        "Toe Raise"
    ],

    "foot": [
        "Ankle Rotation",
        "Ankle Flexion",
        "Heel Raise",
        "Toe Raise"
    ],

    "hip": [
        "Hip Rotation",
        "Hip Stretch",
        "Hip Abduction",
        "Standing Leg Raise"
    ],

    "back": [
        "Upper Back Stretch",
        "Lower Back Stretch",
        "Side Bend"
    ],

    "neck": [
        "Neck Stretch",
        "Neck Rotation",
        "Chin Tuck"
    ],

    "leg": [
        "Straight Leg Raise",
        "Seated Leg Raise",
        "Heel Raise",
        "Toe Raise",
        "Marching in Place"
    ],

    "arm": [
        "Arm Raise Exercise",
        "Arm Stretch",
        "Arm Circles",
        "Shoulder Stretch"
    ],

    "stiffness": [
        "Gentle Full-Body Stretch",
        "Neck Stretch",
        "Shoulder Stretch",
        "Hip Stretch",
        "Calf Stretch"
    ],

    "balance": [
        "Balance Stand",
        "Marching in Place"
    ],

    "weakness": [
        "Seated Leg Raise",
        "Arm Raise Exercise",
        "Marching in Place",
        "Gentle Full-Body Stretch"
    ],

    "flexibility": [
        "Gentle Full-Body Stretch",
        "Shoulder Stretch",
        "Hip Stretch",
        "Calf Stretch",
        "Neck Stretch"
    ],

    "lowerbody": [
        "Knee Extension",
        "Straight Leg Raise",
        "Hip Abduction",
        "Heel Raise"
    ],

    "upperbody": [
        "Shoulder Stretch",
        "Arm Raise Exercise",
        "Arm Circles",
        "Wrist Rotation"
    ],

    "injury": [
        "Gentle Full-Body Stretch",
        "Seated Leg Raise",
        "Shoulder Stretch"
    ],

    "surgery": [
        "Gentle Full-Body Stretch",
        "Seated Leg Raise",
        "Arm Stretch"
    ],

    "limitedmotion": [
        "Gentle Full-Body Stretch",
        "Shoulder Stretch",
        "Hip Stretch",
        "Neck Stretch"
    ],

    "standing": [
        "Seated Leg Raise",
        "Balance Stand",
        "Marching in Place"
    ],

    "walking": [
        "Marching in Place",
        "Balance Stand",
        "Heel Raise",
        "Toe Raise"
    ],

    "sitstand": [
        "Seated Leg Raise",
        "Mini Squat",
        "Marching in Place"
    ],

    "coordination": [
        "Marching in Place",
        "Balance Stand",
        "Arm Circles"
    ],

    "daily": [
        "Gentle Full-Body Stretch",
        "Marching in Place",
        "Seated Leg Raise"
    ],

    "senior": [
        "Seated Leg Raise",
        "Balance Stand",
        "Shoulder Stretch",
        "Marching in Place"
    ],

    "home": [
        "Gentle Full-Body Stretch",
        "Seated Leg Raise",
        "Arm Raise Exercise",
        "Marching in Place"
    ],

    "fullbody": [
        "Gentle Full-Body Stretch",
        "Marching in Place",
        "Shoulder Stretch",
        "Seated Leg Raise"
    ]
}


# =========================================================
# 200 SENTENCE-BASED SYMPTOMS
# =========================================================

SYMPTOMS = {

    "fever": {
        "category": "general",
        "advice": "You may have a fever. Take adequate rest and drink enough fluids. If the fever is high, persistent, or getting worse, consult a doctor."
    },

    "headache": {
        "category": "general",
        "advice": "You may have a headache. Rest in a quiet place and drink enough fluids. If the headache is severe, persistent, or unusual, consult a doctor."
    },

    "body pain": {
        "category": "general",
        "advice": "You may be experiencing body pain. Take adequate rest and avoid overexertion. If the pain is severe or persistent, consult a doctor."
    },

    "cough": {
        "category": "general",
        "advice": "You may have a cough. Rest and drink enough fluids. If the cough is severe, persistent, or associated with breathing difficulty, consult a doctor."
    },

    "cold": {
        "category": "general",
        "advice": "You may have cold-like symptoms. Take rest and drink enough fluids. If symptoms become severe or persistent, consult a doctor."
    },

    "chills": {
        "category": "general",
        "advice": "You may be experiencing chills. Rest and keep yourself comfortably warm. If chills continue or occur with fever, consult a doctor."
    },

    "sore throat": {
        "category": "general",
        "advice": "You may have throat irritation. Drink enough fluids and take adequate rest. If swallowing becomes difficult or symptoms persist, consult a doctor."
    },

    "runny nose": {
        "category": "general",
        "advice": "You may have a runny nose. Rest and drink enough fluids. If symptoms persist or become severe, consult a doctor."
    },

    "blocked nose": {
        "category": "general",
        "advice": "You may have nasal congestion. Rest and drink enough fluids. If breathing becomes difficult, seek medical advice."
    },

    "sneezing": {
        "category": "general",
        "advice": "You may be experiencing sneezing. Try to avoid possible irritants and rest. If symptoms continue, consult a doctor."
    },

    "itchy eyes": {
        "category": "general",
        "advice": "You may have eye irritation. Avoid rubbing your eyes and rest them. If pain or vision problems occur, consult a doctor."
    },

    "nausea": {
        "category": "general",
        "advice": "You may be experiencing nausea. Rest and take fluids in small amounts. If vomiting continues or you cannot keep fluids down, consult a doctor."
    },

    "vomiting": {
        "category": "general",
        "advice": "You are experiencing vomiting. Rest and take small amounts of fluid if you can. If vomiting continues or you become very weak, consult a doctor."
    },

    "diarrhea": {
        "category": "general",
        "advice": "You may have diarrhea. Drink enough fluids to help prevent dehydration. If it is severe, persistent, or you notice blood, consult a doctor."
    },

    "stomach pain": {
        "category": "general",
        "advice": "You have stomach discomfort or pain. Rest and avoid activities that make it worse. If the pain is severe or persistent, consult a doctor."
    },

    "abdominal pain": {
        "category": "general",
        "advice": "You have abdominal pain. Rest and monitor the symptom. If the pain is severe, sudden, or persistent, consult a doctor."
    },

    "chest pain": {
        "category": "general",
        "advice": "Chest pain should not be ignored. Stop strenuous activity and tell a parent or guardian. Seek prompt medical attention, especially if the pain is severe or accompanied by breathing difficulty."
    },

    "breathing difficulty": {
        "category": "general",
        "advice": "You are having difficulty breathing. Stop physical activity and tell a parent or guardian. Seek prompt medical attention if breathing difficulty is significant or worsening."
    },

    "wheezing": {
        "category": "general",
        "advice": "You are experiencing wheezing. Rest and avoid strenuous activity. If breathing becomes difficult or symptoms worsen, seek medical attention."
    },

    "fatigue": {
        "category": "weakness",
        "advice": "You may be experiencing fatigue. Get adequate rest, sleep, and fluids. If tiredness is persistent or affects daily activities, consult a doctor."
    },

    "weakness": {
        "category": "weakness",
        "advice": "You may be experiencing weakness. Rest and maintain adequate food and fluid intake. If weakness is severe or persistent, consult a doctor."
    },

    "dizziness": {
        "category": "balance",
        "advice": "You are experiencing dizziness. Sit or lie down safely and avoid risky activities. If dizziness is severe, repeated, or associated with fainting, consult a doctor."
    },

    "fainting": {
        "category": "balance",
        "advice": "Fainting needs medical attention. Sit or lie down safely and tell a parent or guardian. Seek medical advice, especially if it happens again."
    },

    "back pain": {
        "category": "back",
        "advice": "You may be experiencing back pain. Rest from activities that increase the pain and avoid overexertion. If pain is severe or persistent, consult a doctor."
    },

    "joint pain": {
        "category": "stiffness",
        "advice": "You may be experiencing joint pain. Rest the affected area and avoid movements that increase pain. If pain or swelling persists, consult a doctor."
    },

    "muscle pain": {
        "category": "stiffness",
        "advice": "You may be experiencing muscle pain. Rest and avoid overexertion. If the pain is severe or persistent, consult a doctor."
    },

    "swelling": {
        "category": "stiffness",
        "advice": "You have swelling in part of your body. Rest the affected area and avoid activities that worsen it. If swelling is severe or persistent, consult a doctor."
    },

    "stiffness": {
        "category": "stiffness",
        "advice": "You may be experiencing stiffness. Gentle movement may help if it is comfortable. If stiffness persists or causes difficulty moving, consult a doctor."
    },

    "rash": {
        "category": "general",
        "advice": "You have a skin rash. Avoid scratching and note whether it changes. If it spreads quickly, becomes severe, or persists, consult a doctor."
    },

    "itching": {
        "category": "general",
        "advice": "You are experiencing itching. Avoid scratching the affected area and avoid possible irritants. If it persists or becomes severe, consult a doctor."
    },

    "redness": {
        "category": "general",
        "advice": "You have redness on your skin. Avoid irritating the area. If redness spreads, becomes painful, or persists, consult a doctor."
    },

    "ear pain": {
        "category": "general",
        "advice": "You have ear pain. Avoid putting objects into the ear. If pain is severe or persistent, consult a doctor."
    },

    "hearing difficulty": {
        "category": "general",
        "advice": "You are having difficulty hearing. Avoid loud sounds and inform a parent or guardian. Consult a doctor if the problem persists."
    },

    "tooth pain": {
        "category": "general",
        "advice": "You have tooth pain. Maintain normal oral hygiene and avoid foods that increase the pain. Consult a dentist if the pain persists."
    },

    "swollen gums": {
        "category": "general",
        "advice": "Your gums appear swollen. Maintain gentle oral hygiene and avoid irritating foods. If swelling persists, consult a dentist."
    },

    "painful urination": {
        "category": "general",
        "advice": "You are experiencing pain while urinating. Drink fluids normally and tell a parent or guardian. Consult a doctor if the symptom continues."
    },

    "frequent urination": {
        "category": "general",
        "advice": "You are urinating more frequently than usual. Monitor the symptom and maintain normal fluid intake. If it persists, consult a doctor."
    },

    "lower abdominal pain": {
        "category": "general",
        "advice": "You have lower abdominal pain. Rest and monitor the symptom. If pain is severe, sudden, or persistent, consult a doctor."
    },

    "phlegm": {
        "category": "general",
        "advice": "You have phlegm when coughing. Drink enough fluids and rest. If phlegm persists or breathing becomes difficult, consult a doctor."
    },

    "light sensitivity": {
        "category": "general",
        "advice": "Bright light is making your eyes uncomfortable. Rest your eyes and reduce exposure to bright light. If severe or persistent, consult a doctor."
    },

    "swollen glands": {
        "category": "general",
        "advice": "You may have swollen glands. Rest and monitor the symptom. If swelling persists, becomes painful, or worsens, consult a doctor."
    },

    "dehydration": {
        "category": "weakness",
        "advice": "You may be dehydrated. Drink fluids regularly and rest. If you cannot keep fluids down or feel very weak, seek medical advice."
    },

    "pale skin": {
        "category": "weakness",
        "advice": "You have noticed unusually pale skin. Rest and tell a parent or guardian. If this continues or occurs with weakness or dizziness, consult a doctor."
    },

    "balance problem": {
        "category": "balance",
        "advice": "You are having a balance problem. Avoid activities where you could fall and tell a parent or guardian. If it continues, consult a doctor."
    },

    "loss of appetite": {
        "category": "general",
        "advice": "You have a reduced appetite. Take enough fluids and try small regular meals. If it continues, consult a doctor."
    },

    "weight change": {
        "category": "general",
        "advice": "You have noticed a change in weight. Tell a parent or guardian and monitor the change. If it is unexplained or persistent, consult a doctor."
    },

    "sweating": {
        "category": "general",
        "advice": "You are sweating more than usual. Rest and drink enough fluids. If excessive sweating continues or occurs with other symptoms, consult a doctor."
    },

    "night sweats": {
        "category": "general",
        "advice": "You are experiencing night sweating. Keep your sleeping area comfortable and monitor the symptom. If it continues, consult a doctor."
    },

    "dry mouth": {
        "category": "general",
        "advice": "Your mouth feels dry. Drink fluids regularly and maintain normal oral hygiene. If dryness persists, consult a doctor."
    },

    "thirst": {
        "category": "general",
        "advice": "You are feeling unusually thirsty. Drink fluids regularly. If excessive thirst continues, consult a doctor."
    },

    "dry cough": {
        "category": "general",
        "advice": "You have a dry cough. Rest and drink enough fluids. If the cough persists or breathing becomes difficult, consult a doctor."
    },

    "wet cough": {
        "category": "general",
        "advice": "You have a cough with mucus. Rest and drink enough fluids. If it persists or becomes severe, consult a doctor."
    },

    "hoarse voice": {
        "category": "general",
        "advice": "Your voice sounds hoarse. Rest your voice and drink enough fluids. If it persists, consult a doctor."
    },

    "difficulty swallowing": {
        "category": "general",
        "advice": "You are having difficulty swallowing. Tell a parent or guardian. If swallowing becomes very difficult or breathing is affected, seek prompt medical attention."
    },

    "stuffy nose": {
        "category": "general",
        "advice": "Your nose feels stuffy. Rest and drink enough fluids. If symptoms persist or breathing becomes difficult, consult a doctor."
    },

    "sinus pressure": {
        "category": "general",
        "advice": "You are experiencing sinus pressure. Rest and drink enough fluids. If pain or pressure persists, consult a doctor."
    },

    "facial pain": {
        "category": "general",
        "advice": "You have facial pain. Rest and monitor the symptom. If pain is severe or persistent, consult a doctor."
    },

    "sneezing attacks": {
        "category": "general",
        "advice": "You are having repeated sneezing attacks. Avoid possible irritants and rest. If symptoms persist, consult a doctor."
    },

    "watery eyes": {
        "category": "general",
        "advice": "Your eyes are watering frequently. Avoid rubbing them and reduce exposure to irritants. If the problem persists, consult a doctor."
    },

    "eye redness": {
        "category": "general",
        "advice": "Your eyes look red or irritated. Avoid rubbing them. If there is pain, discharge, or vision change, consult a doctor."
    },

    "eye pain": {
        "category": "general",
        "advice": "You have eye pain. Avoid rubbing your eyes and tell a parent or guardian. Consult a doctor if the pain persists or is severe."
    },

    "blurred vision": {
        "category": "general",
        "advice": "Your vision is blurred. Stop activities that require clear vision and tell a parent or guardian. Consult a doctor if it persists or is sudden."
    },

    "double vision": {
        "category": "general",
        "advice": "You are experiencing double vision. Tell a parent or guardian and avoid activities where clear vision is important. Seek medical advice promptly."
    },

    "ear discharge": {
        "category": "general",
        "advice": "There is unusual discharge from your ear. Do not put objects into the ear. Tell a parent or guardian and consult a doctor."
    },

    "ringing in ears": {
        "category": "general",
        "advice": "You are hearing ringing or buzzing in your ears. Avoid loud sounds. If it continues, consult a doctor."
    },

    "ear fullness": {
        "category": "general",
        "advice": "Your ear feels blocked or full. Avoid putting anything into the ear. If the feeling persists, consult a doctor."
    },

    "tooth sensitivity": {
        "category": "general",
        "advice": "Your teeth are sensitive to hot or cold foods. Avoid triggers and maintain normal oral hygiene. Consult a dentist if it persists."
    },

    "jaw pain": {
        "category": "general",
        "advice": "You have jaw pain. Avoid excessive chewing and rest your jaw. If the pain persists, consult a doctor or dentist."
    },

    "bad breath": {
        "category": "general",
        "advice": "You have persistent bad breath. Maintain good oral hygiene and drink enough water. If it continues, consult a dentist."
    },

    "mouth sores": {
        "category": "general",
        "advice": "You have sores inside your mouth. Avoid irritating foods and maintain gentle oral hygiene. If they persist, consult a doctor or dentist."
    },

    "tongue pain": {
        "category": "general",
        "advice": "Your tongue feels painful. Avoid irritating foods and maintain oral hygiene. If pain persists, consult a doctor or dentist."
    },

    "dry throat": {
        "category": "general",
        "advice": "Your throat feels dry. Drink enough fluids and rest your voice. If the symptom persists, consult a doctor."
    },

    "enlarged tonsils": {
        "category": "general",
        "advice": "Your tonsils appear enlarged. Rest and drink enough fluids. If swallowing or breathing becomes difficult, seek medical attention."
    },

    "voice changes": {
        "category": "general",
        "advice": "Your voice has changed. Rest your voice and drink enough fluids. If the change persists, consult a doctor."
    },

    "neck pain": {
        "category": "neck",
        "advice": "You have neck pain. Avoid sudden neck movements and rest comfortably. If pain is severe or persistent, consult a doctor."
    },

    "neck stiffness": {
        "category": "neck",
        "advice": "Your neck feels stiff. Avoid forcing the movement and rest comfortably. If stiffness is severe or persistent, consult a doctor."
    },

    "shoulder pain": {
        "category": "shoulder",
        "advice": "You have shoulder pain. Rest the shoulder and avoid movements that increase pain. If pain persists, consult a doctor."
    },

    "arm pain": {
        "category": "arm",
        "advice": "You have arm pain. Rest the affected arm and avoid overexertion. If pain is severe or persistent, consult a doctor."
    },

    "elbow pain": {
        "category": "arm",
        "advice": "You have elbow pain. Rest the affected arm and avoid movements that increase pain. If it persists, consult a doctor."
    },

    "wrist pain": {
        "category": "wrist",
        "advice": "You have wrist pain. Rest the wrist and avoid activities that increase pain. If symptoms persist, consult a doctor."
    },

    "hand pain": {
        "category": "hand",
        "advice": "You have hand pain. Rest your hand and avoid overuse. If pain persists or movement becomes difficult, consult a doctor."
    },

    "finger pain": {
        "category": "hand",
        "advice": "You have finger pain. Rest the affected finger and avoid activities that increase pain. If it persists, consult a doctor."
    },

    "hip pain": {
        "category": "hip",
        "advice": "You have hip pain. Avoid movements that increase pain and rest comfortably. If pain persists, consult a doctor."
    },

    "knee pain": {
        "category": "knee",
        "advice": "You have knee pain. Rest the knee and avoid activities that increase pain. If pain is severe or persistent, consult a doctor."
    },

    "leg pain": {
        "category": "leg",
        "advice": "You have leg pain. Rest the affected leg and avoid overexertion. If pain is severe or persistent, consult a doctor."
    },

    "calf pain": {
        "category": "leg",
        "advice": "You have calf pain. Rest the affected leg and avoid strenuous activity. If the pain is severe or persistent, consult a doctor."
    },

    "ankle pain": {
        "category": "ankle",
        "advice": "You have ankle pain. Rest the ankle and avoid activities that increase pain. If swelling or pain persists, consult a doctor."
    },

    "foot pain": {
        "category": "foot",
        "advice": "You have foot pain. Rest the foot and avoid activities that increase pain. If it persists, consult a doctor."
    },

    "heel pain": {
        "category": "foot",
        "advice": "You have heel pain. Rest your foot and avoid activities that increase pain. If it persists, consult a doctor."
    },

    "muscle cramps": {
        "category": "leg",
        "advice": "You are experiencing muscle cramps. Rest the affected muscle and drink enough fluids. If cramps happen repeatedly, consult a doctor."
    },

    "muscle stiffness": {
        "category": "stiffness",
        "advice": "Your muscles feel stiff. Gentle movement may help if comfortable. If stiffness persists or worsens, consult a doctor."
    },

    "muscle tenderness": {
        "category": "stiffness",
        "advice": "Your muscles feel tender. Rest and avoid overexertion. If tenderness is severe or persistent, consult a doctor."
    },

    "joint swelling": {
        "category": "stiffness",
        "advice": "You have swelling around a joint. Rest the affected area and avoid activities that increase discomfort. Consult a doctor if it persists."
    },

    "joint tenderness": {
        "category": "stiffness",
        "advice": "Your joints feel tender. Rest the affected area and avoid overexertion. If symptoms persist, consult a doctor."
    },

    "reduced movement": {
        "category": "limitedmotion",
        "advice": "You have reduced movement in a body part. Do not force the movement. If it persists or worsens, consult a doctor."
    },

    "limited mobility": {
        "category": "limitedmotion",
        "advice": "You have limited mobility. Move only within a comfortable range and avoid forcing movement. Consult a doctor if it persists."
    },

    "difficulty walking": {
        "category": "walking",
        "advice": "You are having difficulty walking. Avoid unsafe walking and tell a parent or guardian. If the problem is new or worsening, consult a doctor."
    },

    "difficulty standing": {
        "category": "standing",
        "advice": "You are having difficulty standing. Sit safely and avoid overexertion. If this is new or persistent, consult a doctor."
    },

    "difficulty climbing stairs": {
        "category": "leg",
        "advice": "You are having difficulty climbing stairs. Avoid overexertion and use support when needed. If this continues, consult a doctor."
    },

    "difficulty bending": {
        "category": "back",
        "advice": "You are having difficulty bending. Avoid forcing the movement. If the problem persists or causes pain, consult a doctor."
    },

    "difficulty lifting": {
        "category": "arm",
        "advice": "You are having difficulty lifting objects. Avoid heavy lifting and rest the affected area. If it persists, consult a doctor."
    },

    "difficulty reaching": {
        "category": "shoulder",
        "advice": "You are having difficulty reaching. Avoid forcing the shoulder movement. If it persists or causes pain, consult a doctor."
    },

    "difficulty gripping": {
        "category": "hand",
        "advice": "You are having difficulty gripping objects. Rest your hand and avoid overuse. If the problem persists, consult a doctor."
    },

    "difficulty holding objects": {
        "category": "hand",
        "advice": "You are having difficulty holding objects. Avoid carrying heavy objects and tell a parent or guardian. If it persists, consult a doctor."
    },

    "tremor": {
        "category": "coordination",
        "advice": "You are experiencing shaking or tremor. Avoid activities where this could cause injury and tell a parent or guardian. If it persists, consult a doctor."
    },

    "shaking": {
        "category": "coordination",
        "advice": "You are experiencing shaking. Rest safely and tell a parent or guardian. If shaking continues or is severe, consult a doctor."
    },

    "poor coordination": {
        "category": "coordination",
        "advice": "You are having difficulty coordinating movements. Avoid unsafe activities and tell a parent or guardian. If it persists, consult a doctor."
    },

    "numbness": {
        "category": "general",
        "advice": "You are experiencing numbness. Avoid activities where reduced sensation could cause injury. Tell a parent or guardian and consult a doctor if it persists."
    },

    "tingling": {
        "category": "general",
        "advice": "You are experiencing tingling. Monitor the symptom and avoid pressure on the affected area. If it persists or worsens, consult a doctor."
    },

    "burning sensation": {
        "category": "general",
        "advice": "You are experiencing a burning sensation. Avoid irritating the affected area. If it persists or worsens, consult a doctor."
    },

    "reduced sensation": {
        "category": "general",
        "advice": "You have reduced sensation in part of your body. Avoid activities where this could cause injury. Consult a doctor if it persists."
    },

    "increased sensitivity": {
        "category": "general",
        "advice": "The affected area feels more sensitive than usual. Avoid irritating it. If the symptom persists, consult a doctor."
    },

    "cold hands": {
        "category": "hand",
        "advice": "Your hands feel unusually cold. Keep them comfortably warm and monitor the symptom. If it continues, consult a doctor."
    },

    "cold feet": {
        "category": "foot",
        "advice": "Your feet feel unusually cold. Keep them comfortably warm and monitor the symptom. If it continues, consult a doctor."
    },

    "weak grip": {
        "category": "hand",
        "advice": "Your grip feels weaker than usual. Avoid heavy objects and rest your hand. If weakness persists, consult a doctor."
    },

    "muscle weakness": {
        "category": "weakness",
        "advice": "You may be experiencing muscle weakness. Rest and avoid overexertion. If weakness is persistent or worsening, consult a doctor."
    },

    "leg weakness": {
        "category": "leg",
        "advice": "Your legs feel weak. Avoid unsafe walking and tell a parent or guardian. If weakness is new or worsening, consult a doctor."
    },

    "arm weakness": {
        "category": "arm",
        "advice": "Your arms feel weak. Avoid lifting heavy objects and tell a parent or guardian. If weakness is new or worsening, consult a doctor."
    },

    "difficulty balancing": {
        "category": "balance",
        "advice": "You are having difficulty balancing. Avoid activities where you could fall and tell a parent or guardian. If it persists, consult a doctor."
    },

    "unsteady walking": {
        "category": "walking",
        "advice": "Your walking feels unsteady. Sit safely and avoid walking without support if needed. Tell a parent or guardian and consult a doctor."
    },

    "sleepiness": {
        "category": "general",
        "advice": "You feel unusually sleepy. Get adequate rest and sleep. If excessive sleepiness persists, consult a doctor."
    },

    "insomnia": {
        "category": "general",
        "advice": "You are having difficulty sleeping. Maintain a regular sleep routine and reduce screen use before bed. If it persists, consult a doctor."
    },

    "poor sleep": {
        "category": "general",
        "advice": "You are not sleeping well. Try a regular sleep schedule and adequate rest. If the problem continues, consult a doctor."
    },

    "restlessness": {
        "category": "general",
        "advice": "You are feeling restless. Take time to rest and maintain a regular routine. If it persists, talk to a parent or guardian and consult a doctor."
    },

    "irritability": {
        "category": "general",
        "advice": "You are feeling more irritable than usual. Get adequate rest and maintain regular meals and sleep. If it persists, talk to a parent or guardian."
    },

    "confusion": {
        "category": "general",
        "advice": "You are experiencing confusion. Tell a parent or guardian. If confusion is sudden or significant, seek medical attention promptly."
    },

    "difficulty concentrating": {
        "category": "general",
        "advice": "You are having difficulty concentrating. Get adequate sleep, food, fluids, and breaks. If it persists, talk to a parent or guardian and consult a doctor."
    },

    "memory difficulty": {
        "category": "general",
        "advice": "You are having difficulty remembering things. Tell a parent or guardian and monitor the symptom. If it persists, consult a doctor."
    },

    "low energy": {
        "category": "weakness",
        "advice": "You have low energy. Get adequate rest, food, fluids, and sleep. If low energy persists, consult a doctor."
    },

    "general discomfort": {
        "category": "general",
        "advice": "You are experiencing general discomfort. Rest and monitor your symptoms. If the discomfort persists or worsens, consult a doctor."
    },

    "abdominal bloating": {
        "category": "general",
        "advice": "You are experiencing abdominal bloating. Eat slowly and maintain normal fluid intake. If bloating is persistent or painful, consult a doctor."
    },

    "gas": {
        "category": "general",
        "advice": "You are experiencing gas or abdominal discomfort. Eat slowly and monitor which foods affect you. If it persists, consult a doctor."
    },

    "indigestion": {
        "category": "general",
        "advice": "You may be experiencing indigestion. Eat smaller meals and avoid foods that worsen the discomfort. If it persists, consult a doctor."
    },

    "heartburn": {
        "category": "general",
        "advice": "You are experiencing heartburn. Avoid foods that trigger the discomfort and avoid lying down immediately after eating. If it persists, consult a doctor."
    },

    "acid reflux": {
        "category": "general",
        "advice": "You are experiencing acid reflux symptoms. Avoid trigger foods and avoid lying down immediately after meals. If symptoms persist, consult a doctor."
    },

    "constipation": {
        "category": "general",
        "advice": "You may have constipation. Drink enough fluids and include normal dietary fiber. If it persists or is painful, consult a doctor."
    },

    "loose stools": {
        "category": "general",
        "advice": "You have loose stools. Drink enough fluids and rest. If the problem persists or becomes severe, consult a doctor."
    },

    "abdominal cramps": {
        "category": "general",
        "advice": "You are experiencing abdominal cramps. Rest and monitor the symptom. If cramps are severe or persistent, consult a doctor."
    },

    "feeling full quickly": {
        "category": "general",
        "advice": "You are feeling full quickly after eating. Eat slowly and monitor the symptom. If it continues, consult a doctor."
    },

    "stomach burning": {
        "category": "general",
        "advice": "You are experiencing stomach burning. Avoid foods that worsen the discomfort and monitor the symptom. If it persists, consult a doctor."
    },

    "stomach discomfort": {
        "category": "general",
        "advice": "You have stomach discomfort. Rest and monitor what foods affect it. If discomfort persists or becomes severe, consult a doctor."
    },

    "blood in stool": {
        "category": "general",
        "advice": "You noticed blood in your stool. Tell a parent or guardian. You should consult a doctor for proper evaluation."
    },

    "black stool": {
        "category": "general",
        "advice": "Your stool appears unusually black. Tell a parent or guardian and consult a doctor, especially if this is new or persistent."
    },

    "nausea after eating": {
        "category": "general",
        "advice": "You feel nauseous after eating. Rest and take fluids in small amounts. If it continues, consult a doctor."
    },

    "vomiting after eating": {
        "category": "general",
        "advice": "You are vomiting after eating. Rest and take small amounts of fluid if possible. If it continues, consult a doctor."
    },

    "excessive thirst": {
        "category": "general",
        "advice": "You are experiencing excessive thirst. Drink fluids regularly and monitor the symptom. If it continues, consult a doctor."
    },

    "frequent hunger": {
        "category": "general",
        "advice": "You are feeling hungry more frequently than usual. Maintain regular meals and monitor the symptom. If it persists, consult a doctor."
    },

    "frequent bowel movements": {
        "category": "general",
        "advice": "You are having bowel movements more frequently than usual. Maintain normal fluid intake. If this persists, consult a doctor."
    },

    "difficulty passing stool": {
        "category": "general",
        "advice": "You are having difficulty passing stool. Drink enough fluids and maintain normal dietary fiber. If it persists, consult a doctor."
    },

    "skin dryness": {
        "category": "general",
        "advice": "Your skin feels dry. Use gentle skin care and maintain normal fluid intake. If dryness persists or becomes severe, consult a doctor."
    },

    "skin peeling": {
        "category": "general",
        "advice": "Your skin is peeling. Avoid scratching or irritating the area. If peeling is widespread or persistent, consult a doctor."
    },

    "skin irritation": {
        "category": "general",
        "advice": "Your skin is irritated. Avoid possible irritants and scratching. If irritation persists or worsens, consult a doctor."
    },

    "skin swelling": {
        "category": "general",
        "advice": "Some skin areas appear swollen. Avoid irritating the area. If swelling is severe, spreading, or persistent, consult a doctor."
    },

    "skin tenderness": {
        "category": "general",
        "advice": "Your skin feels tender. Avoid pressure or irritation. If tenderness persists or worsens, consult a doctor."
    },

    "skin discoloration": {
        "category": "general",
        "advice": "You have noticed a change in skin colour. Monitor the area and tell a parent or guardian. If it persists, consult a doctor."
    },

    "blisters": {
        "category": "general",
        "advice": "You have blisters on your skin. Avoid popping them and protect the area from irritation. If they worsen or become infected-looking, consult a doctor."
    },

    "hives": {
        "category": "general",
        "advice": "You have raised itchy patches on your skin. Avoid known irritants and tell a parent or guardian. If swelling affects breathing, seek emergency medical attention."
    },

    "acne": {
        "category": "general",
        "advice": "You have acne spots. Keep the skin clean and avoid squeezing the spots. If acne is severe or persistent, consult a doctor."
    },

    "hair loss": {
        "category": "general",
        "advice": "You have noticed increased hair loss. Avoid harsh hair treatments and tell a parent or guardian. If it continues, consult a doctor."
    },

    "excessive sweating": {
        "category": "general",
        "advice": "You are sweating excessively. Drink enough fluids and stay comfortable. If it continues or affects daily activities, consult a doctor."
    },

    "reduced sweating": {
        "category": "general",
        "advice": "You are sweating less than usual. Stay in a comfortable environment and monitor the symptom. If it persists, consult a doctor."
    },

    "feverish feeling": {
        "category": "general",
        "advice": "You feel feverish. Check your temperature if possible, rest, and drink enough fluids. If fever is high or persistent, consult a doctor."
    },

    "feeling cold": {
        "category": "general",
        "advice": "You are feeling unusually cold. Rest and keep yourself comfortably warm. If this continues or occurs with other symptoms, consult a doctor."
    },

    "feeling hot": {
        "category": "general",
        "advice": "You are feeling unusually hot. Rest in a comfortable environment and drink enough fluids. If this continues, consult a doctor."
    },

    "shivering": {
        "category": "general",
        "advice": "You are experiencing shivering. Rest and keep yourself comfortably warm. If it continues or occurs with fever, consult a doctor."
    },

    "head pressure": {
        "category": "general",
        "advice": "You feel pressure in your head. Rest and drink enough fluids. If it is severe, persistent, or unusual, consult a doctor."
    },

    "facial swelling": {
        "category": "general",
        "advice": "Your face appears swollen. Tell a parent or guardian and monitor the symptom. If swelling is sudden or affects breathing, seek medical attention promptly."
    },

    "eye swelling": {
        "category": "general",
        "advice": "The area around your eyes appears swollen. Avoid rubbing your eyes. If swelling is severe, painful, or affects vision, consult a doctor."
    },

    "eye discharge": {
        "category": "general",
        "advice": "You have unusual eye discharge. Avoid rubbing your eyes and maintain good hygiene. If it persists or vision changes, consult a doctor."
    },

    "dry eyes": {
        "category": "general",
        "advice": "Your eyes feel dry. Take regular screen breaks and avoid rubbing them. If dryness persists, consult a doctor."
    },

    "loss of smell": {
        "category": "general",
        "advice": "You have noticed a loss of smell. Monitor the symptom and tell a parent or guardian. If it persists, consult a doctor."
    },

    "reduced smell": {
        "category": "general",
        "advice": "Your sense of smell seems weaker than usual. Monitor the symptom. If it persists, consult a doctor."
    },

    "loss of taste": {
        "category": "general",
        "advice": "You have noticed a loss of taste. Monitor the symptom and tell a parent or guardian. If it persists, consult a doctor."
    },

    "reduced taste": {
        "category": "general",
        "advice": "Your sense of taste seems weaker than usual. Monitor the symptom. If it persists, consult a doctor."
    },

    "difficulty breathing during activity": {
        "category": "general",
        "advice": "You become short of breath during activity. Stop and rest. Tell a parent or guardian, and consult a doctor if this keeps happening."
    },

    "shortness of breath": {
        "category": "general",
        "advice": "You are experiencing shortness of breath. Stop strenuous activity and rest. Tell a parent or guardian and seek medical advice if it persists or worsens."
    },

    "rapid breathing": {
        "category": "general",
        "advice": "You are breathing faster than usual. Stop activity and rest. Tell a parent or guardian and seek medical advice if it continues."
    },

    "palpitations": {
        "category": "general",
        "advice": "You can feel your heartbeat unusually strongly or quickly. Rest and tell a parent or guardian. If it continues or is associated with chest pain or fainting, seek medical attention."
    },

    "fast heartbeat": {
        "category": "general",
        "advice": "Your heartbeat feels faster than usual. Rest and tell a parent or guardian. If it persists or occurs with other concerning symptoms, seek medical advice."
    },

    "irregular heartbeat": {
        "category": "general",
        "advice": "Your heartbeat feels irregular. Rest and tell a parent or guardian. Consult a doctor for proper evaluation."
    },

    "low energy during activity": {
        "category": "weakness",
        "advice": "You have low energy during activity. Rest and avoid overexertion. If this continues, tell a parent or guardian and consult a doctor."
    },

    "exercise intolerance": {
        "category": "weakness",
        "advice": "You become tired unusually quickly during exercise. Stop when uncomfortable and rest. If this keeps happening, consult a doctor."
    },

    "chest tightness": {
        "category": "general",
        "advice": "You are experiencing chest tightness. Stop strenuous activity and tell a parent or guardian. Seek prompt medical attention if it is severe or associated with breathing difficulty."
    },

    "chest discomfort": {
        "category": "general",
        "advice": "You have chest discomfort. Stop strenuous activity and tell a parent or guardian. If it persists or is severe, seek medical attention."
    },

    "difficulty taking deep breaths": {
        "category": "general",
        "advice": "You are having difficulty taking a deep breath. Stop activity and rest. Tell a parent or guardian and seek medical advice if it persists."
    },

    "pain while breathing": {
        "category": "general",
        "advice": "You have pain while breathing. Stop strenuous activity and tell a parent or guardian. Seek medical advice promptly."
    },

    "voice weakness": {
        "category": "general",
        "advice": "Your voice feels weak. Rest your voice and drink enough fluids. If the problem persists, consult a doctor."
    },

    "general weakness": {
        "category": "weakness",
        "advice": "You are experiencing general weakness. Rest and maintain adequate food, fluids, and sleep. If weakness persists or worsens, consult a doctor."
    },

    "morning stiffness": {
        "category": "stiffness",
        "advice": "You feel stiff in the morning. Gentle movement may help if comfortable. If the stiffness is persistent or painful, consult a doctor."
    },

    "movement-related pain": {
        "category": "stiffness",
        "advice": "You feel pain when moving. Avoid movements that increase the pain and rest. If it persists, consult a doctor."
    },

    "pain after activity": {
        "category": "stiffness",
        "advice": "You experience pain after activity. Rest and avoid overexertion. If the pain repeatedly occurs or persists, consult a doctor."
    },

    "pain at rest": {
        "category": "general",
        "advice": "You are experiencing pain even while resting. Tell a parent or guardian. If the pain is severe or persistent, consult a doctor."
    },

    "difficulty sleeping due to pain": {
        "category": "general",
        "advice": "Pain is affecting your sleep. Rest and tell a parent or guardian. If the pain continues, consult a doctor."
    },

    "reduced range of motion": {
        "category": "limitedmotion",
        "advice": "You have reduced range of motion. Do not force the joint or body part. If movement remains limited, consult a doctor."
    },

    "muscle fatigue": {
        "category": "weakness",
        "advice": "Your muscles become tired quickly. Rest and avoid overexertion. If this continues, consult a doctor."
    },

    "joint discomfort": {
        "category": "stiffness",
        "advice": "You have joint discomfort. Rest the affected area and avoid movements that increase discomfort. If it persists, consult a doctor."
    },

    "general body stiffness": {
        "category": "stiffness",
        "advice": "Your body feels stiff. Gentle movement may help if comfortable. If stiffness persists or affects daily activities, consult a doctor."
    },

    "difficulty performing daily activities": {
        "category": "daily",
        "advice": "You are having difficulty with normal daily activities. Avoid overexertion and tell a parent or guardian. If this continues, consult a doctor."
    },

    "tired and weak": {
        "category": "weakness",
        "advice": "You feel tired and weak after simple activities. Rest and maintain adequate food, fluids, and sleep. If this persists, consult a doctor."
    },

    "difficulty moving comfortably": {
        "category": "daily",
        "advice": "You are having difficulty moving comfortably during daily activities. Avoid forcing movements and rest. If this persists, consult a doctor."
    }
}


# =========================================================
# HOME PAGE
# =========================================================

@app.route("/")
def home():
    return render_template("index.html")


# =========================================================
# GET EXERCISES
# =========================================================

@app.route("/get_exercises", methods=["POST"])
def get_exercises():

    data = request.get_json()

    condition = str(
        data.get("condition", "")
    ).strip().lower()

    exercises = CONDITION_EXERCISES.get(
        condition,
        []
    )

    return jsonify({
        "exercises": exercises
    })


# =========================================================
# SYMPTOM ANALYSIS
# =========================================================

@app.route("/analyze", methods=["POST"])
def analyze():

    data = request.get_json()

    user_text = str(
        data.get("symptoms", "")
    ).strip().lower()

    # Remove extra spaces
    user_text = " ".join(
        user_text.split()
    )

    if not user_text:

        return jsonify({
            "message": "Please enter your symptoms."
        })


    found_symptoms = []

    found_categories = []

    advice_list = []


    # Check every symptom
    for symptom, information in SYMPTOMS.items():

        if symptom in user_text:

            found_symptoms.append(symptom)

            category = information["category"]

            if category not in found_categories:

                found_categories.append(
                    category
                )

            if information["advice"] not in advice_list:

                advice_list.append(
                    information["advice"]
                )


    # Nothing detected
    if not found_symptoms:

        return jsonify({

            "message":
                "I could not find a matching symptom. Please describe your symptom more clearly.",

            "symptoms": [],

            "categories": [],

            "advice": [],

            "exercises": []

        })


    # Get exercises
    exercises = []

    for category in found_categories:

        category_exercises = CONDITION_EXERCISES.get(
            category,
            []
        )

        for exercise in category_exercises:

            if exercise not in exercises:

                exercises.append(exercise)


    return jsonify({

        "message":
            "Possible general information based on the symptoms you entered. This is not a medical diagnosis.",

        "symptoms":
            found_symptoms,

        "categories":
            found_categories,

        "advice":
            advice_list,

        "exercises":
            exercises

    })


# =========================================================
# REHABILITATION FEEDBACK
# =========================================================

@app.route("/rehab_feedback", methods=["POST"])
def rehab_feedback():

    data = request.get_json()

    exercise = str(
        data.get("exercise", "")
    ).strip()

    try:

        angle = float(
            data.get("angle", 0)
        )

    except:

        angle = 0


    if exercise not in EXERCISES:

        return jsonify({

            "feedback":
                "Exercise not found."

        })


    exercise_data = EXERCISES[exercise]

    minimum = exercise_data["min"]

    maximum = exercise_data["max"]


    if angle < minimum:

        feedback = exercise_data["low"]

    elif angle > maximum:

        feedback = "Move a little lower."

    else:

        feedback = exercise_data["good"]


    return jsonify({

        "feedback":
            feedback

    })


# =========================================================
# RUN
# =========================================================

if __name__ == "__main__":

    app.run(
        debug=True
    )