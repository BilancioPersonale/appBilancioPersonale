

#
# class Bl_BudgetManagement_Budget(db.Model):
#     ID_Budget = db.Colum(db.Integer, primary_key=True, autoincrement=True)
#     Budget_Name = db.Column(db.String(50), unique=True, nullable=False)
#     FK_ID_User = db.Column(db.Integer, db.ForeignKey(''))
#
# class Bl_BudgetManagement_Movement(db.Model):
#     ID_Movement = db.Colum(db.Integer, primary_key=True, autoincrement=True)
#     Movement_Name = db.Column(db.String(50), unique=True, nullable=False)
#     Movement_Date = db.Column(db.DateTime, unique=True, nullable=False)
#     Movement_Amount = db.Column(db.Float(2), unique=True, nullable=False)
#     Movement_Type = db.Column(db.String(50), unique=True, nullable=False)
#     FK_ID_User = db.Column(db.Integer, db.ForeignKey('users.py'))
#



# """
# CREATE TABLE Bl_BudgetManagement_Budget
#   (
#     ID_Budget INTEGER PRIMARY KEY AUTOINCREMENT,
#     Budget_Name VARCHAR2(50) NOT NULL,
#     FK_ID_User INTEGER NOT NULL
#   );
#   CREATE TABLE Bl_BudgetManagement_Movement
#     (
#       ID_Movement INTEGER PRIMARY KEY AUTOINCREMENT,
#       Movement_Name VARCHAR2(50) NOT NULL,
#       Movement_Date DATE NOT NULL,
#       Movement_Amount FLOAT(2) NOT NULL,
#       Movement_Type VARCHAR2(50) NOT NULL
#     );
# CREATE ADD weeeen
# """