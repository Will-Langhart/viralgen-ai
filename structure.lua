viralgen-ai/
│── backend/                              # Django/Flask backend
│   │── app.py                            # Main application file
│   │── models.py                         # Database models
│   │── routes/                           # API routes
│   │   │── content.py                     # AI-generated social media content
│   │   │── automation.py                   # Auto-posting logic
│   │── services/                          # Business logic
│   │   │── openai_service.py               # AI-generated captions & tweets
│   │   │── video_generator.py              # AI video scripts
│   │── config.py                          # Configuration settings
│   │── database.py                        # PostgreSQL setup
│   │── requirements.txt                   # Dependencies
│   └── tests/                             # Unit tests
│
│── frontend/                             # Next.js/React frontend
│   │── pages/                            # UI pages
│   │   │── index.js                       # Home page
│   │   │── scheduler.js                    # Auto-post scheduler UI
│   │── components/                        # UI Components
│   │   │── CaptionForm.js                   # Caption generator
│   │   │── VideoEditor.js                   # AI script editor
│   │── styles/                            # Tailwind CSS styles
│   │── package.json                       # Frontend dependencies
│   └── tests/                             # Unit tests for frontend
│
│── docs/                                 # Documentation
│── README.md                             # Project overview
└── Dockerfile                            # Containerization setup
