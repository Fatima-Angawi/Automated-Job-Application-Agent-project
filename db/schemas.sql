-- Basic schemas for storing jobs and applicants

CREATE TABLE IF NOT EXISTS jobs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    company TEXT,
    location TEXT,
    url TEXT UNIQUE NOT NULL,
    summary TEXT,
    posted_date TEXT,
    raw JSON
);

CREATE TABLE IF NOT EXISTS applicants (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    phone TEXT,
    resume_json JSON,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS applications (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    job_id INTEGER REFERENCES jobs(id),
    applicant_id INTEGER REFERENCES applicants(id),
    status TEXT,
    applied_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
