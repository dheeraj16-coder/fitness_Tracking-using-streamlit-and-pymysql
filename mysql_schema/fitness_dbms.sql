use fitness_tracking;
CREATE TABLE `users` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `age` int NOT NULL,
  `height` int NOT NULL,
  `weight` int NOT NULL,
  `gender` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `activity_level` varchar(255) NOT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `exercise_log` (
  `workout_id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `calories_burnt` int NOT NULL default 0,
  `time` varchar(255) NOT NULL,
  `date` date NOT NULL,
  `workout_type` varchar(255) NOT NULL,
  PRIMARY KEY (`workout_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `exercise_log_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `exercises` (
  `exercise_id` int NOT NULL AUTO_INCREMENT,
  `exercise_name` varchar(255) NOT NULL,
  `met_value` decimal(10,2) NOT NULL,
  `calories_burnt_per_minute` decimal(10,2) NOT NULL,
  PRIMARY KEY (`exercise_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `foods` (
  `food_id` int NOT NULL AUTO_INCREMENT,
  `food_name` varchar(255) NOT NULL,
  `fat` decimal(10,2) NOT NULL,
  `protein` decimal(10,2) NOT NULL,
  `carbohydrates` decimal(10,2) NOT NULL,
  `calories_per_Serving` decimal(10,2) NOT NULL,
  `type` enum('v','nv') NOT NULL,
  PRIMARY KEY (`food_id`)
) ENGINE=InnoDB AUTO_INCREMENT=62 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `exercise_log_exercise` (
  `workout_id` int NOT NULL,
  `exercise_id` int NOT NULL,
  `duration` int NOT NULL,
  PRIMARY KEY (`workout_id`,`exercise_id`),
  KEY `exercise_id` (`exercise_id`),
  CONSTRAINT `exercise_log_exercise_ibfk_1` FOREIGN KEY (`workout_id`) REFERENCES `exercise_log` (`workout_id`),
  CONSTRAINT `exercise_log_exercise_ibfk_2` FOREIGN KEY (`exercise_id`) REFERENCES `exercises` (`exercise_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `goals` (
  `goal_id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `calories_target` int NOT NULL default 0,
  `goal_type` varchar(255) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `end_date` date NOT NULL,
  `start_date` date NOT NULL,
  PRIMARY KEY (`goal_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `goals_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `meals` (
  `meal_id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `calories_consumed` int NOT NULL default 0,
  `time` datetime NOT NULL,
  `meal_type` varchar(255) NOT NULL,
  `date` date NOT NULL,
  PRIMARY KEY (`meal_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `meals_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `meal_log_food` (
  `meal_id` int NOT NULL,
  `food_id` int NOT NULL,
  `servings_size` int NOT NULL,
  PRIMARY KEY (`meal_id`,`food_id`),
  KEY `food_id` (`food_id`),
  CONSTRAINT `meal_log_food_ibfk_1` FOREIGN KEY (`meal_id`) REFERENCES `meals` (`meal_id`),
  CONSTRAINT `meal_log_food_ibfk_2` FOREIGN KEY (`food_id`) REFERENCES `foods` (`food_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO foods (food_name, calories_per_Serving, protein, fat, carbohydrates, type)
VALUES ('Congee', 150, 5, 0, 30,'v');
INSERT INTO foods (food_name, calories_per_Serving, protein, fat, carbohydrates, type)
VALUES ('Miso soup', 70, 5, 0, 15,'v');
INSERT INTO foods (food_name, calories_per_Serving, protein, fat, carbohydrates, type)
VALUES ('Onigiri', 180, 5, 2, 30,'v');
INSERT INTO foods (food_name, calories_per_Serving, protein, fat, carbohydrates, type)
VALUES ('Pork buns', 300, 10, 10, 40,'nv');
INSERT INTO foods (food_name, calories_per_Serving, protein, fat, carbohydrates, type)
VALUES ('Spring rolls', 200, 5, 10, 30,'nv');
INSERT INTO foods (food_name, calories_per_Serving, protein, fat, carbohydrates, type)
VALUES ('Bibimbap', 500, 20, 20, 80,'nv');
INSERT INTO foods (food_name, calories_per_Serving, protein, fat, carbohydrates, type)
VALUES ('Pad thai', 500, 20, 20, 80,'v');
INSERT INTO foods (food_name, calories_per_Serving, protein, fat, carbohydrates, type)
VALUES ('Pho', 400, 20, 10, 60,'v');
INSERT INTO foods (food_name, calories_per_Serving, protein, fat, carbohydrates, type)
VALUES ('Sushi', 300, 10, 5, 50,'nv');
INSERT INTO foods (food_name, calories_per_Serving, protein, fat, carbohydrates, type)
VALUES ('typeeggie dumplings', 200, 5, 10, 30,'nv');
INSERT INTO foods (food_name, calories_per_Serving, protein, fat, carbohydrates, type)
VALUES ('Chicken curry', 500, 30, 20, 60,'nv');
INSERT INTO foods (food_name, calories_per_Serving, protein, fat, carbohydrates, type)
VALUES ('Fish stir-fry', 400, 20, 10, 60,'nv');
INSERT INTO foods (food_name, calories_per_Serving, protein, fat, carbohydrates, type)
VALUES ('Fried rice', 500, 20, 20, 80,'v');
INSERT INTO foods (food_name, calories_per_Serving, protein, fat, carbohydrates, type)
VALUES ('Japanese curry', 500, 30, 20, 60,'v');
INSERT INTO foods (food_name, calories_per_Serving, protein, fat, carbohydrates, type)
VALUES ('typeegetarian stir-fry', 400, 20, 10, 60,'v');

INSERT INTO users (name, age, height, weight, gender, activity_level,password)
VALUES ('John Doe', 35, 180, 90, 'Male', 'Moderately active',12345);

INSERT INTO users (name, age, height, weight, gender, activity_level,password)
VALUES ('Jane Doe', 25, 160, 55, 'Female', 'Sedentary',1234);

INSERT INTO goals (user_id, goal_type, calories_target, start_date, end_date,created_at,updated_at)
VALUES (1, 'Lose weight', 10, '2023-10-23', '2024-01-23',curdate(),curdate());

INSERT INTO goals (user_id, goal_type, calories_target, start_date, end_date,created_at,updated_at)
VALUES (2, 'Gain muscle', 5, '2023-10-30', '2024-04-30',curdate(),curdate());

ALTER TABLE meals MODIFY time TIME;

-- Insert breakfast for user ID 1
INSERT INTO meals (user_id, meal_type, time, date, calories_consumed)
VALUES (1, 'Breakfast', '09:00:00', '2023-10-24', 0);

-- Insert lunch for user ID 1
INSERT INTO meals (user_id, meal_type, time, date, calories_consumed)
VALUES (1, 'Lunch', '12:00:00', '2023-10-24', 0);

-- Insert dinner for user ID 1
INSERT INTO meals (user_id, meal_type, time, date, calories_consumed)
VALUES (1, 'Dinner', '19:00:00', '2023-10-24', 0);

-- Insert breakfast for user ID 2
INSERT INTO meals (user_id, meal_type, time, date, calories_consumed)
VALUES (2, 'Breakfast', '09:00:00', '2023-10-24', 0);

-- Insert lunch for user ID 2
INSERT INTO meals (user_id, meal_type, time, date, calories_consumed)
VALUES (2, 'Lunch', '12:00:00', '2023-10-24', 0);

-- Insert dinner for user ID 2
INSERT INTO meals (user_id, meal_type, time, date, calories_consumed)
VALUES (2, 'Dinner', '19:00:00', '2023-10-24', 0);

UPDATE `trail1`.`foods` SET `food_id` = '1' WHERE (`food_id` = '62');
UPDATE `trail1`.`foods` SET `food_id` = '2' WHERE (`food_id` = '63');
UPDATE `trail1`.`foods` SET `food_id` = '3' WHERE (`food_id` = '64');
UPDATE `trail1`.`foods` SET `food_id` = '4' WHERE (`food_id` = '65');
UPDATE `trail1`.`foods` SET `food_id` = '5' WHERE (`food_id` = '66');
UPDATE `trail1`.`foods` SET `food_id` = '6' WHERE (`food_id` = '67');
UPDATE `trail1`.`foods` SET `food_id` = '7' WHERE (`food_id` = '68');
UPDATE `trail1`.`foods` SET `food_id` = '8' WHERE (`food_id` = '69');
UPDATE `trail1`.`foods` SET `food_id` = '9' WHERE (`food_id` = '70');
UPDATE `trail1`.`foods` SET `food_id` = '10' WHERE (`food_id` = '71');
UPDATE `trail1`.`foods` SET `food_id` = '11' WHERE (`food_id` = '72');
UPDATE `trail1`.`foods` SET `food_id` = '12' WHERE (`food_id` = '73');
UPDATE `trail1`.`foods` SET `food_id` = '13' WHERE (`food_id` = '74');
UPDATE `trail1`.`foods` SET `food_id` = '14' WHERE (`food_id` = '75');
UPDATE `trail1`.`foods` SET `food_id` = '15' WHERE (`food_id` = '76');

INSERT INTO meal_log_food (meal_id, food_id, servings_size)
VALUES
(1, 2, 3),
(1, 3, 2),
(1, 4, 1),
(2,6,1),
(3,8,1),
(4,10,2),
(5,12,1),
(6,15,2);

INSERT INTO foods (food_name, fat, protein, carbohydrates, calories_per_serving, type)
VALUES ('Dosa', 5.3, 12.1, 63.6, 263, 'v');

INSERT INTO foods (food_name, fat, protein, carbohydrates, calories_per_serving, type)
VALUES ('Poha', 4.2, 9.6, 62.3, 252, 'v');

INSERT INTO foods (food_name, fat, protein, carbohydrates, calories_per_serving, type)
VALUES ('Upma', 3.5, 7.2, 61.3, 241, 'v');

INSERT INTO foods (food_name, fat, protein, carbohydrates, calories_per_serving, type)
VALUES ('Paratha', 6.5, 14.2, 60.3, 271, 'v');

INSERT INTO foods (food_name, fat, protein, carbohydrates, calories_per_serving, type)
VALUES ('Omelet', 10.5, 15.2, 61.3, 283, 'nv');

INSERT INTO foods (food_name, fat, protein, carbohydrates, calories_per_serving, type)
VALUES ('Chicken or lamb kebabs', 15.5, 20.2, 62.3, 293, 'nv');

INSERT INTO foods (food_name, fat, protein, carbohydrates, calories_per_serving, type)
VALUES ('Fish curry', 12.5, 18.2, 59.3, 273, 'nv');

INSERT INTO foods (food_name, fat, protein, carbohydrates, calories_per_serving, type)
VALUES ('Dal makhani', 10.5, 25.2, 65.3, 345, 'v');

INSERT INTO foods (food_name, fat, protein, carbohydrates, calories_per_serving, type)
VALUES ('Vegetable biryani', 11.5, 26.2, 64.3, 355, 'v');

INSERT INTO foods (food_name, fat, protein, carbohydrates, calories_per_serving, type)
VALUES ('Aloo gobi', 12.5, 27.2, 63.3, 365, 'v');

INSERT INTO foods (food_name, fat, protein, carbohydrates, calories_per_serving, type)
VALUES ('Palak paneer', 13.5, 28.2, 62.3, 375, 'v');

INSERT INTO foods (food_name, fat, protein, carbohydrates, calories_per_serving, type)
VALUES ('Chicken tikka masala', 20.3, 32.1, 45.6, 423, 'nv');

INSERT INTO foods (food_name, fat, protein, carbohydrates, calories_per_serving, type)
VALUES ('Butter chicken', 19.3, 31.1, 44.6, 413, 'nv');

INSERT INTO foods (food_name, fat, protein, carbohydrates, calories_per_serving, type)
VALUES ('Lamb rogan josh', 18.3, 30.1, 43.6, 403, 'nv');

INSERT INTO foods (food_name, fat, protein, carbohydrates, calories_per_serving, type)
VALUES ('Fish curry', 17.3, 29.1, 42.6, 393, 'nv');
INSERT INTO foods (food_name, fat, protein, carbohydrates, calories_per_serving, type)
VALUES ('Oats upma', 3.5, 7.2, 61.3, 241, 'v');

INSERT INTO foods (food_name, fat, protein, carbohydrates, calories_per_serving, type)
VALUES ('Multigrain paratha', 6.5, 14.2, 60.3, 271, 'v');

INSERT INTO foods (food_name, fat, protein, carbohydrates, calories_per_serving, type)
VALUES ('Vegetable poha', 4.2, 9.6, 62.3, 252, 'v');

INSERT INTO foods (food_name, fat, protein, carbohydrates, calories_per_serving, type)
VALUES ('Sprouts chila', 3.5, 7.2, 61.3, 241, 'v');

INSERT INTO foods (food_name, fat, protein, carbohydrates, calories_per_serving, type)
VALUES ('Lentil soup', 3.5, 9.2, 63.3, 253, 'v');

INSERT INTO foods (food_name, fat, protein, carbohydrates, calories_per_serving, type)
VALUES ('Chicken breast curry', 15.5, 28.2, 62.3, 293, 'nv');

INSERT INTO foods (food_name, fat, protein, carbohydrates, calories_per_serving, type)
VALUES ('Fish tikka', 12.5, 26.2, 61.3, 273, 'nv');

INSERT INTO foods (food_name, fat, protein, carbohydrates, calories_per_serving, type)
VALUES ('Tandoori chicken', 10.5, 25.2, 60.3, 253, 'nv');

INSERT INTO foods (food_name, fat, protein, carbohydrates, calories_per_serving, type)
VALUES ('Quinoa pulao', 4.5, 10.2, 65.3, 245, 'v');

INSERT INTO foods (food_name, fat, protein, carbohydrates, calories_per_serving, type)
VALUES ('Brown rice with vegetables', 5.3, 12.1, 63.6, 263, 'v');

INSERT INTO foods (food_name, fat, protein, carbohydrates, calories_per_serving, type)
VALUES ('Khichdi', 4.2, 9.6, 62.3, 252, 'v');

INSERT INTO foods (food_name, fat, protein, carbohydrates, calories_per_serving, type)
VALUES ('Ragi roti', 3.5, 7.2, 61.3, 241, 'v');

INSERT INTO foods (food_name, fat, protein, carbohydrates, calories_per_serving, type)
VALUES ('Dal tadka', 3.5, 9.2, 63.3, 253, 'v');

INSERT INTO exercises (exercise_name, met_value, calories_burnt_per_minute)
VALUES
    ('Running', 8.0, 0.7),
    ('Walking', 3.5, 0.3),
    ('Biking', 6.0, 0.5),
    ('Swimming', 5.5, 0.4),
    ('Dancing', 4.0, 0.3),
    ('Yoga', 3.0, 0.2),
    ('Pilates', 3.5, 0.2),
    ('Strength training', 4.0, 0.3),
    ('HIIT', 7.0, 0.6),
    ('Zumba', 5.0, 0.4),
    ('Kickboxing', 6.5, 0.5),
    ('Boxing', 7.5, 0.6),
    ('Elliptical', 6.0, 0.5),
    ('Rowing machine', 7.0, 0.6),
    ('Stair climber', 7.5, 0.6),
    ('Jumping rope', 8.0, 0.7),
    ('Burpees', 7.5, 0.6),
    ('Lunges', 4.0, 0.3),
    ('Squats', 4.5, 0.4),
    ('Push-ups', 4.0, 0.3),
    ('Pull-ups', 5.0, 0.4),
    ('Plank', 3.5, 0.2),
    ('Cobra pose', 2.0, 0.1),
    ('Cat-cow pose', 2.5, 0.2),
    ('Downward-facing dog', 3.0, 0.2),
    ('Warrior I pose', 3.5, 0.2),
    ('Warrior II pose', 4.0, 0.3),
    ('Tree pose', 4.5, 0.4),
    ('Bridge pose', 5.0, 0.4),
    ('Wheel pose', 5.5, 0.4),
    ('Headstand', 6.0, 0.5),
    ('Handstand', 6.5, 0.5);
    INSERT INTO exercises (exercise_name, met_value, calories_burnt_per_minute)
VALUES
  ('Jumping jacks', 8.0, 0.7),
  ('High knees', 8.5, 0.7),
  ('Butt kicks', 8.0, 0.7),
  ('Mountain climbers', 9.0, 0.8),
  ('Jumping rope', 10.0, 0.9),
  ('Star jumps', 9.5, 0.8),
  ('Burpees', 10.0, 0.9),
  ('Sprints', 11.0, 1.0),
  ('Elliptical trainer', 8.0, 0.7),
  ('Rowing machine', 8.5, 0.7),
  ('Stair climber', 9.0, 0.8),
  ('Swimming', 8.0, 0.7),
  ('Biking', 8.0, 0.7),
  ('Running', 8.0, 0.7),
  ('Dancing', 8.0, 0.7),
  ('Push-ups', 8.0, 0.7),
  ('Pull-ups', 8.0, 0.7),
  ('Squats', 8.0, 0.7),
  ('Lunges', 8.0, 0.7),
  ('Plank', 8.0, 0.7);

--procedure creation command for goal setting

CREATE PROCEDURE CalculateCaloriesTarget(
    IN p_user_id INT,
    IN p_goal_type VARCHAR(255),
    IN p_end_date DATE
)
BEGIN
    -- Declare variables
    DECLARE v_start_date DATE;
    DECLARE v_calories_target INT;
    DECLARE v_goal_exists INT DEFAULT 0;
    DECLARE v_duration_factor DECIMAL(10, 2);

    -- Set start_date to the current date
    SET v_start_date = CURDATE();

    -- Calculate calories_target based on user weight, activity level, and goal type
    SELECT
        CASE
            WHEN p_goal_type = 'Weight Loss' THEN
                CASE
                    WHEN u.activity_level = 'sedentary' THEN u.weight * 8
                    WHEN u.activity_level = 'medium active' THEN u.weight * 10
                    WHEN u.activity_level = 'active' THEN u.weight * 12
                    ELSE u.weight * 10  -- Default for unknown activity level
                END
            WHEN p_goal_type = 'Maintenance' THEN
                CASE
                    WHEN u.activity_level = 'sedentary' THEN u.weight * 10
                    WHEN u.activity_level = 'medium active' THEN u.weight * 12
                    WHEN u.activity_level = 'active' THEN u.weight * 14
                    ELSE u.weight * 12  -- Default for unknown activity level
                END
            WHEN p_goal_type = 'Muscle Gain' THEN
                CASE
                    WHEN u.activity_level = 'sedentary' THEN u.weight * 12
                    WHEN u.activity_level = 'medium active' THEN u.weight * 14
                    WHEN u.activity_level = 'active' THEN u.weight * 16
                    ELSE u.weight * 14  -- Default for unknown activity level
                END
            ELSE u.weight * 10  -- Default for unknown goal type
        END INTO v_calories_target
    FROM users u
    WHERE u.user_id = p_user_id;

    -- Check if a goal already exists for the user
    SELECT COUNT(*) INTO v_goal_exists FROM goals WHERE user_id = p_user_id;

    -- Calculate the duration factor based on the difference in days
    SET v_duration_factor = DATEDIFF(p_end_date, v_start_date) / 30.44;  -- Assuming an average month length

    -- Adjust calories_target based on duration factor
    SET v_calories_target = v_calories_target * v_duration_factor;

    -- If a goal exists, update it; otherwise, insert a new goal
    IF v_goal_exists > 0 THEN
        UPDATE goals
        SET calories_target = v_calories_target,
            goal_type = p_goal_type,
            end_date = p_end_date,
            updated_at = NOW()
        WHERE user_id = p_user_id;
    ELSE
        INSERT INTO goals (user_id, calories_target, goal_type, start_date, end_date, created_at, updated_at)
        VALUES (p_user_id, v_calories_target, p_goal_type, v_start_date, p_end_date, NOW(), NOW());
    END IF;

    -- Return the calculated calories_target
    SELECT v_calories_target AS calories_target;
END //

DELIMITER ;

--triggers creation for calories_consumed update

DELIMITER //

CREATE TRIGGER recalculate_calories
AFTER UPDATE ON meal_log_food
FOR EACH ROW
BEGIN
    DECLARE total_calories_consumed DECIMAL(10, 2);

    -- Calculate total calories consumed for the meal
    SELECT 
        SUM((f.calories_per_Serving * mlf.servings_size) + (f.fat * 9 * mlf.servings_size) + 
            (f.protein * 4 * mlf.servings_size) + (f.carbohydrates * 4 * mlf.servings_size))
    INTO total_calories_consumed
    FROM foods f
    JOIN meal_log_food mlf ON f.food_id = mlf.food_id
    WHERE mlf.meal_id = NEW.meal_id;

    -- Update the total calories consumed for the meal
    UPDATE meals
    SET calories_consumed = total_calories_consumed
    WHERE meal_id = NEW.meal_id;
END;
//

DELIMITER ;

--trigger for calories_burnt update

DELIMITER //

CREATE TRIGGER update_calories_burnt 
AFTER UPDATE ON exercise_log_exercise
FOR EACH ROW
BEGIN
  DECLARE total_calories_burned DECIMAL(10, 2);

  -- Calculate the total calories burned for the workout
  SELECT SUM(
    (e.met_value * ele.duration) + (e.calories_burnt_per_minute * ele.duration)
  )
  INTO total_calories_burned
  FROM exercise_log_exercise ele
  JOIN exercises e ON ele.exercise_id = e.exercise_id
  WHERE ele.workout_id = NEW.workout_id;

  -- Update the calories_burnt field in the exercise_log table
  UPDATE exercise_log
  SET calories_burnt = total_calories_burned
  WHERE workout_id = NEW.workout_id;
END //

DELIMITER ;
