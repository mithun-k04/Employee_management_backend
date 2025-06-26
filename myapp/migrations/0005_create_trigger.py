from django.db import migrations

trigger_sql = """
DROP TRIGGER IF EXISTS create_leave_records;

CREATE TRIGGER create_leave_records
AFTER INSERT ON myapp_employee
FOR EACH ROW
BEGIN
<<<<<<< HEAD
  INSERT INTO myapp_leavemodel (employee, month, sl, cl)
=======
  INSERT INTO myapp_leavemodel (employee_id, month, sl, cl)
>>>>>>> 62506c085f34622a671ae78a64637786ee561545
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
END;
"""

class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_leavemodel'),  
    ]

    operations = [
        migrations.RunSQL(trigger_sql),
    ]
