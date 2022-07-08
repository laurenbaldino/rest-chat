DROP TABLE IF EXISTS suspended_users;
DROP TABLE IF EXISTS messages;
DROP TABLE IF EXISTS channel_messages;
DROP TABLE IF EXISTS channels;
DROP TABLE IF EXISTS users_to_communities;
DROP TABLE IF EXISTS communities;
DROP TABLE IF EXISTS users;


CREATE TABLE users
(
  user_id SERIAL PRIMARY KEY,
  email VARCHAR UNIQUE NOT NULL,
  username VARCHAR UNIQUE NOT NULL,
  passwrd VARCHAR NOT NULL,
  created_on DATE,
  changed_on DATE,
  change_end DATE,
  session_key VARCHAR
)
;

CREATE TABLE communities
(
  community_id SERIAL PRIMARY KEY,
  name VARCHAR UNIQUE NOT NULL
)
;

CREATE TABLE users_to_communities
(
  user_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE,
  community_id INTEGER REFERENCES communities(community_id) ON DELETE CASCADE
)
;

CREATE TABLE channels
(
  channel_id SERIAL PRIMARY KEY,
  name VARCHAR UNIQUE NOT NULL,
  community_id INTEGER REFERENCES communities(community_ID) ON DELETE CASCADE
)
;

CREATE TABLE channel_messages
(
  message_id SERIAL PRIMARY KEY,
  sender_id INTEGER REFERENCES users(user_ID) ON DELETE CASCADE,
  channel_id INTEGER REFERENCES channels(channel_ID) ON DELETE CASCADE,
  message VARCHAR NOT NULL,
  sent_on DATE,
  is_read BOOLEAN
)
;

CREATE TABLE messages
(
  message_id SERIAL PRIMARY KEY,
  sender_id INTEGER REFERENCES users(user_ID) ON DELETE CASCADE,
  reciever_id INTEGER REFERENCES users(user_ID) ON DELETE CASCADE,
  message VARCHAR NOT NULL,
  sent_on DATE,
  is_read BOOLEAN
)
;

CREATE TABLE suspended_users
(
  user_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE,
  community_id INTEGER REFERENCES communities(community_id) ON DELETE CASCADE,
  suspension_end DATE
)
;











