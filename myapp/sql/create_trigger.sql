DROP TRIGGER IF EXISTS create_leave_records;

DELIMITER $$

CREATE TRIGGER create_leave_records
AFTER INSERT ON myapp_employee
FOR EACH ROW
BEGIN
  INSERT INTO myapp_leavemodel (employee_id, month, sl, cl)
  VALUES 
    (NEW.id, 'January', 0, 0),
    (NEW.id, 'February', 0, 0),
    (NEW.id, 'March', 0, 0),
    (NEW.id, 'April', 0, 0),
    (NEW.id, 'May', 0, 0),
    (NEW.id, 'June', 0, 0),
    (NEW.id, 'July', 0, 0),
    (NEW.id, 'August', 0, 0),
    (NEW.id, 'September', 0, 0),
    (NEW.id, 'October', 0, 0),
    (NEW.id, 'November', 0, 0),
    (NEW.id, 'December', 0, 0);
END$$

DELIMITER ;
