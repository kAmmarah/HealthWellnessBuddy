# Wellness App - AI-Powered Personal Health Platform

## Overview

This is a full-stack wellness application that combines a React frontend with an Express.js backend to provide personalized health and fitness recommendations. The app uses Google's Gemini AI to generate custom wellness plans based on user goals and preferences, featuring a modern UI built with shadcn/ui components and Tailwind CSS.

**Status**: Fully functional with Gemini AI integration active and all features operational.

## User Preferences

Preferred communication style: Simple, everyday language.

## Recent Changes

**January 11, 2025**
- ✓ Configured Google Gemini AI integration with user-provided API key
- ✓ Migrated from in-memory storage to PostgreSQL database with Drizzle ORM
- ✓ Created database schema and pushed tables to production database
- ✓ Updated storage layer to use DatabaseStorage with proper SQL queries
- ✓ Verified all API endpoints working with persistent database storage
- ✓ Confirmed AI-powered wellness plan generation functional with database persistence
- ✓ Daily task auto-creation system operational with database backing
- ✓ Real-time AI insights generation working with database integration
- ✓ Added comprehensive progress tracking with charts and analytics dashboard
- ✓ Implemented Analytics page with Recharts for weight, energy, and workout visualizations
- ✓ Created workout templates system with pre-built templates for all fitness levels
- ✓ Added goal progress tracking with visual progress bars and targets
- ✓ Personalized footer with creator attribution: "Created with ❤️ by Ammara Dawod"
- ✓ Enhanced UI with emojis and modern design elements throughout the application
- ✓ Added Templates page with 6 pre-built workouts (strength, cardio, flexibility)
- ✓ Integrated workout templates with progress tracking system
- ✓ Implemented wellness journey timeline visualization with milestone tracking
- ✓ Added interactive timeline showing goals, achievements, progress, and milestones
- ✓ Enhanced timeline events with emojis and motivational descriptions
- ✓ Integrated timeline with all data sources (progress, workouts, nutrition, goals)
- ✓ Updated dashboard welcome message to "Health & Wellness Planner" with emoji branding
- ✓ Removed generic "Welcome back, Jordan" and replaced with personalized wellness theme
- ✓ Enhanced all UI sections with emojis for better user experience
- ✓ Added motivational welcome message with wellness journey theme

## System Architecture

### Frontend Architecture
- **Framework**: React 18 with TypeScript
- **Routing**: Wouter for lightweight client-side routing
- **UI Components**: shadcn/ui component library with Radix UI primitives
- **Styling**: Tailwind CSS with custom design tokens and CSS variables
- **State Management**: TanStack Query (React Query) for server state management
- **Form Handling**: React Hook Form with Zod validation
- **Build Tool**: Vite with custom configuration for development and production

### Backend Architecture
- **Framework**: Express.js with TypeScript
- **Database**: PostgreSQL with Drizzle ORM
- **Database Provider**: Neon Database (serverless PostgreSQL)
- **API Structure**: RESTful endpoints under `/api` prefix
- **Middleware**: Express middleware for JSON parsing, CORS, and request logging

### Data Storage Solutions
- **Database**: PostgreSQL with Neon Database (serverless provider)
- **ORM**: Drizzle ORM for type-safe database operations
- **Schema**: Shared TypeScript schema definitions using Drizzle and Zod
- **Migration**: Drizzle Kit for database schema migrations (`npm run db:push`)
- **Storage Interface**: Abstract storage layer with DatabaseStorage implementation using real PostgreSQL

## Key Components

### Database Schema
- **Users**: Basic user authentication and profile data
- **Wellness Goals**: User-defined health objectives with detailed metrics (age, height, weight, activity level)
- **Wellness Plans**: AI-generated personalized plans including nutrition, exercise, and habit strategies
- **Daily Tasks**: Task tracking system for daily wellness activities

### AI Integration
- **Service**: Google Gemini AI integration for generating personalized wellness plans
- **Prompt Engineering**: Structured prompts that consider user goals, physical metrics, and dietary preferences
- **Response Format**: JSON-structured responses for nutrition plans, exercise routines, and habit strategies

### UI Components
- **Dashboard**: Main interface for creating goals and viewing plans
- **Form System**: Multi-step form for capturing user wellness data
- **Component Library**: Complete shadcn/ui implementation with custom styling
- **Responsive Design**: Mobile-first approach with Tailwind breakpoints

## Data Flow

1. **Goal Creation**: User fills out wellness goal form with personal metrics and preferences
2. **AI Processing**: Form data is sent to backend, which calls Gemini AI with structured prompts
3. **Plan Generation**: AI returns personalized nutrition, exercise, and habit recommendations
4. **Data Persistence**: Goals and generated plans are stored in PostgreSQL database
5. **Dashboard Display**: User can view their goals and AI-generated plans on the dashboard

## External Dependencies

### Core Dependencies
- **@google/genai**: Google Gemini AI SDK for generating wellness plans
- **@neondatabase/serverless**: Neon Database driver for PostgreSQL connections
- **drizzle-orm**: Type-safe ORM for database operations
- **@tanstack/react-query**: Server state management and caching

### UI Dependencies
- **@radix-ui/***: Accessible UI primitives for all interactive components
- **tailwindcss**: Utility-first CSS framework
- **class-variance-authority**: Type-safe component variants
- **react-hook-form**: Form handling with validation

### Development Dependencies
- **vite**: Fast build tool with HMR support
- **tsx**: TypeScript execution for development server
- **esbuild**: Fast bundling for production builds

## Deployment Strategy

### Development Setup
- **Frontend**: Vite dev server with HMR and error overlay
- **Backend**: tsx for running TypeScript server with hot reload
- **Database**: Environment-based PostgreSQL connection via DATABASE_URL
- **Environment**: Separate NODE_ENV configurations for development/production

### Production Build
- **Frontend**: Vite production build to `dist/public`
- **Backend**: esbuild compilation to `dist/index.js`
- **Static Assets**: Served by Express in production mode
- **Database**: Production PostgreSQL instance via environment variables

### Key Configuration Files
- **drizzle.config.ts**: Database configuration and migration settings
- **vite.config.ts**: Frontend build configuration with path aliases
- **tsconfig.json**: TypeScript configuration with shared paths
- **tailwind.config.ts**: Tailwind CSS configuration with custom design tokens

The application follows a modern full-stack architecture with clear separation of concerns, type safety throughout the stack, and a focus on developer experience and user interface quality.