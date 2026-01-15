📘 POOLWISE — Gen-AI Powered Carpooling App

Smart & efficient AI-driven carpooling platform for employees and drivers.

⸻

🚀 Project Overview

PoolWise is a full-stack carpooling solution powered by FastAPI, React Native (Expo), and advanced AI optimization algorithms.
Designed for organizations with daily commuting staff, it solves major pain points like:
	•	❗ Last-minute cancellations
	•	🛣️ Inefficient pickup/drop routes
	•	🚗 Driver–employee matching
	•	💸 Payment tracking
	•	⏰ Schedule conflicts

The app provides real-time matching, route optimization, driver assignment, and automated notifications using Gen-AI and smart algorithms.

⸻

🧠 Key Features

🔹 For Employees
	•	Request rides in 2 taps
	•	View upcoming & past rides
	•	Book recurring rides
	•	Track pending payments
	•	Real-time driver assignment

🔹 For Drivers
	•	Manage daily availability
	•	View assigned rides
	•	See optimized pickup route
	•	Accept/Reject ride requests
	•	Track payment collections

🔹 AI / Gen-AI Features
	•	Smart driver–employee matching
	•	Dynamic route optimization
	•	Automated conflict resolution (Claude AI)
	•	Real-time notifications (FCM)
	•	Future: demand prediction & dynamic pricing

⸻

🏗️ Tech Stack

Frontend
	•	React Native (Expo)
	•	React Navigation
	•	Zustand for state management
	•	Google Maps API / Mapbox

Backend
	•	FastAPI (Python)
	•	PostgreSQL + SQLAlchemy
	•	Redis (real-time cache)
	•	Alembic migrations
	•	JWT Authentication

AI / ML
	•	OR-Tools (Route Optimization)
	•	scikit-learn (Driver Matching Model)
	•	Claude API (Edge-case decision making)

DevOps & Tools
	•	Git + GitHub
	•	Docker (optional)
	•	Railway / Render (deployment)
	•	Postman / Thunder Client
	•	VS Code

⸻

📂 Project Structure
PoolWise/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── models/
│   │   ├── services/
│   │   ├── ai_engine/
│   │   └── utils/
│   ├── main.py
│   └── requirements.txt
│
├── frontend/
│   ├── app/
│   ├── assets/
│   ├── components/
│   ├── constants/
│   ├── hooks/
│   ├── package.json
│   └── App.js
│
└── README.md
⚙️ Backend Setup (FastAPI)

🧬 AI Features (Planned & Implemented)

Driver–Employee Matching
	•	Distance-based scoring
	•	Availability & time compatibility
	•	Vehicle seat handling
	•	Historical matching model (RandomForest)

Route Optimization
	•	OR-Tools TSP/VRP
	•	Minimizes time & distance
	•	Multi-pickup path ordering

Claude AI Integration
	•	Conflict resolution
	•	Intelligent fallback logic
	•	Dynamic route reassignment

⸻

🚀 Deployment Plan

Backend (Railway / Render)
	•	Connect repo
	•	Add environment variables
	•	Deploy on push

Frontend (Expo)
	•	Expo build for Android / iOS
	•	Internal distribution for testing
	•	App Store / Play Store later

⸻

📅 Development Roadmap (21 Days)

Week 1 — Backend Core

✔ FastAPI setup
✔ DB schema
✔ User auth
✔ Booking system
✔ Smart matching algorithm
✔ Route optimizer

Week 2 — Frontend App

✔ Screens setup
✔ Authentication
✔ Booking flow
✔ Driver UI
✔ Maps integration
✔ API connection

Week 3 — AI + Deployment

✔ AI model training
✔ Claude integration
✔ End-to-end tests
✔ Deployment
✔ Beta testing

⸻

🔮 Future Enhancements
	•	Route optimization with live traffic
	•	Dynamic surge pricing
	•	Employee ride preferences
	•	Driver ratings & reviews
	•	Chat inside each ride
	•	Admin dashboard
	•	Company-level analytics

⸻

🙌 Contributor

Jay Madchetti
Built with ❤️ using FastAPI, React Native & AI.

⸻

⭐ If you like the project, consider giving it a Star on GitHub!

