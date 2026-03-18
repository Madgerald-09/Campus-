# ConfessionWall

An anonymous social network built with Django and Supabase.

## Setup

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Set up Supabase:
   - Create a new project at https://supabase.com
   - Go to Settings > Database
   - Copy the connection string and update `.env`:
     ```
     DATABASE_URL=postgresql://postgres:[password]@db.[project-ref].supabase.co:5432/postgres
     ```

3. Run migrations:

   ```bash
   python manage.py migrate
   ```

4. Run the server:

   ```bash
   python manage.py runserver
   ```

5. Open http://127.0.0.1:8000/

## Features

- Post anonymous confessions
- View all confessions in chronological order
- Beautiful dark UI with Tailwind CSS

## For Supabase Integration

If you want to use Supabase features like real-time updates or authentication, you can extend the app with the Supabase JavaScript client.

Add to your template:

```html
<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
```

And initialize:

```javascript
const supabase = createClient("your-supabase-url", "your-anon-key");
```
