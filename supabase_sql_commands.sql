-- -- Drop in Supabase SQL Editor

-- 1. Clear ALL data but KEEP tables (SAFEST)
DO $$ 
DECLARE
    r RECORD;
BEGIN
    -- Disable triggers temporarily
    EXECUTE 'SET session_replication_role = replica';

    -- Truncate all tables
    FOR r IN (SELECT tablename FROM pg_tables WHERE schemaname = 'public')
    LOOP
        EXECUTE 'TRUNCATE TABLE public.' || quote_ident(r.tablename) || ' CASCADE;';
    END LOOP;

    -- Re-enable triggers
    EXECUTE 'SET session_replication_role = DEFAULT';
END $$;


-- 2. FULL RESET (Delete ALL tables)
-- If you want completely empty schema
DROP SCHEMA public CASCADE;
CREATE SCHEMA public;


-- 3. 
-- ⚠️ DEV ONLY: wipes EVERYTHING inside the public schema (tables, views, functions, policies, triggers)
DROP SCHEMA IF EXISTS public CASCADE;
CREATE SCHEMA public;

-- Restore default Supabase schema permissions (important)
GRANT USAGE ON SCHEMA public TO postgres, anon, authenticated, service_role;
GRANT ALL ON SCHEMA public TO postgres, service_role;

-- Optional but recommended: default privileges for future tables/sequences/functions
ALTER DEFAULT PRIVILEGES IN SCHEMA public
GRANT ALL ON TABLES TO postgres, service_role;

ALTER DEFAULT PRIVILEGES IN SCHEMA public
GRANT ALL ON SEQUENCES TO postgres, service_role;

ALTER DEFAULT PRIVILEGES IN SCHEMA public
GRANT ALL ON FUNCTIONS TO postgres, service_role;


-- 4. Reset via SQL (works even when no “Reset” button)
-- Most recommended for dev
-- Supabase Dashboard → SQL Editor → New query → run:
DROP SCHEMA IF EXISTS public CASCADE;
CREATE SCHEMA public;

-- Supabase baseline roles
GRANT USAGE ON SCHEMA public TO postgres, anon, authenticated, service_role;
GRANT ALL ON SCHEMA public TO postgres, service_role;

-- Optional: make sure future objects are accessible to service_role/postgres
ALTER DEFAULT PRIVILEGES IN SCHEMA public
GRANT ALL ON TABLES TO postgres, service_role;

ALTER DEFAULT PRIVILEGES IN SCHEMA public
GRANT ALL ON SEQUENCES TO postgres, service_role;

ALTER DEFAULT PRIVILEGES IN SCHEMA public
GRANT ALL ON FUNCTIONS TO postgres, service_role;


-- 5. Confirm it’s clean (It should return zero rows.)
SELECT tablename
FROM pg_tables
WHERE schemaname = 'public'
ORDER BY tablename;