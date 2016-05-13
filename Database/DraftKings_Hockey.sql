--DROP TABLE player

CREATE TABLE coach (
	coach_id BIGSERIAL Primary key,
	first_name varchar(60),
	last_name varchar(60)
);

CREATE TABLE skater (
	skater_id BIGSERIAL Primary key,
	first_name varchar(60),
	last_name varchar(60),
	right_stick_side boolean
);

CREATE TABLE goalie (
	goalie_id BIGSERIAL Primary key,
	first_name varchar(60),
	last_name varchar(60),
	right_stick_side boolean
);

CREATE TABLE game (
	game_id BIGSERIAL Primary key,
	game_played_on_date timestamp,
	arena_name varchar(60)
);

CREATE TABLE team (
	team_id BIGSERIAL Primary Key,
	team_name varchar(60)
);

CREATE TABLE skater_game_stats (
	player_game_stat_id BIGSERIAL Primary key,
	skater_id BIGSERIAL REFERENCES skater (skater_id),
	game_id BIGSERIAL REFERENCES game (game_id),
	team_id BIGSERIAL REFERENCES team (team_id),
	coach_id BIGSERIAL REFERENCES coach (coach_id),
	postion char NOT NULL,
	goals smallint NOT NULL DEFAULT 0,
	assists smallint NOT NULL DEFAULT 0,
	shots_on_goal smallint NOT NULL DEFAULT 0,
	block_shots smallint NOT NULL DEFAULT 0,
	short_handed_bonsus smallint NOT NULL DEFAULT 0,
	plus_minus smallint NOT NULL DEFAULT 0,
	penalty_minutes smallint NOT NULL DEFAULT 0,
	powerplay_points smallint NOT NULL DEFAULT 0
);

CREATE TABLE goalie_game_stats (
	goalie_game_stat_id BIGSERIAL Primary key,
	game_id BIGSERIAL REFERENCES game (game_id),
	team_id BIGSERIAL REFERENCES team (team_id),
	coach_id BIGSERIAL REFERENCES coach (coach_id),
	won boolean NOT NULL DEFAULT false,
	goals_against smallint DEFAULT 0,
	saves smallint DEFAULT 0,
	shutout boolean DEFAULT false
);