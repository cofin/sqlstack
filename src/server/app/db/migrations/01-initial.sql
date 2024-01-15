create table user_account
(
    id              uuid                     not null,
    email           varchar                  not null,
    name            varchar,
    hashed_password varchar(255),
    is_active       boolean                  not null,
    is_superuser    boolean                  not null,
    is_verified     boolean                  not null,
    verified_at     date,
    joined_at       date                     not null,
    created_at      timestamp with time zone not null default now(),
    updated_at      timestamp with time zone not null default now(), 
    constraint pk_user_account
        primary key (id)
);

comment on table user_account is 'User accounts for application access';
 
create unique index ix_user_account_email
    on user_account (email);

create table team
(
    id              uuid                     not null,    
    slug            varchar(100)             not null,
    name            varchar                  not null, 
    description     varchar(500),
    is_active       boolean                  not null,
    created_at      timestamp with time zone not null default now(),
    updated_at      timestamp with time zone not null default now(), 
    constraint pk_team
        primary key (id),
    constraint uq_team_slug
        unique (slug)
);
 
create index ix_team_name
    on team (name);

create table team_member
(
    user_id         uuid                     not null,
    team_id    uuid                     not null,
    role            varchar(50)              not null,
    is_owner        boolean                  not null,
    id              uuid                     not null,
    created_at      timestamp with time zone not null default now(),
    updated_at      timestamp with time zone not null default now(), 
    constraint pk_team_member
        primary key (id),
    constraint uq_team_member_user_id
        unique (user_id, team_id),
    constraint fk_team_member_team_id_team
        foreign key (team_id) references team
            on delete cascade,
    constraint fk_team_member_user_id_user_account
        foreign key (user_id) references user_account
            on delete cascade
);
 

create index ix_team_member_role
    on team_member (role);


create table role
(
    id              uuid                     not null,
    slug            varchar(100)             not null,
    name            varchar                  not null,
    description     varchar, 
    is_enabled      boolean                  not null default true,
    created_at      timestamp with time zone not null default now(),
    updated_at      timestamp with time zone not null default now(), 
    constraint pk_role
        primary key (id),
    constraint uq_role_slug
        unique (slug),
    constraint uq_role_name
        unique (name)
);

comment on table role is 'Access roles for the application';
 
 
create table user_account_role
(    
    id              uuid                     not null,
    user_id         uuid                     not null,
    role_id         uuid                     not null,
    assigned_at     timestamp with time zone not null default now(),
    created_at      timestamp with time zone not null default now(),
    updated_at      timestamp with time zone not null default now(), 
    constraint pk_user_account_role
        primary key (id),
    constraint fk_user_account_role_role_id_role
        foreign key (role_id) references role
            on delete cascade,
    constraint fk_user_account_role_user_id_user_account
        foreign key (user_id) references user_account
            on delete cascade
);

comment on table user_account_role is 'Links a user to a specific role.';
 