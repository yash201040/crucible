# security-and-data/hipaa-setup

* [HIPAA configuration: confirmation and what developers see](hipaa-confirmation-and-restrictions.md) - How to confirm the configuration is active and which features turn off, including WebFetch, cloud sessions, feedback, artifacts and credential stripping. **[high]**
* [HIPAA configuration: eligible connections and requirements](hipaa-eligibility-and-connections.md) - The HIPAA configuration applies only to Claude Enterprise sign-ins connecting directly to the Claude API on v2.1.285 or later, plus required network hosts.
* [HIPAA sample managed settings keys](hipaa-managed-settings.md) - Sample managed settings (forceLoginMethod, forceLoginOrgUUID, allowedProviders, cleanupPeriodDays) and sessions they do not block. **[high]**
* [Purge local session data and offboard developers](local-data-purge-and-offboarding.md) - claude purge (v2.1.288+) and claude project purge delete local transcripts and memory; retention sweep runs only at start; removing a seat deletes nothing.
