class Task:
  def __init__(self, t_id):
    self.id = t_id
    self.is_done = false
    
class Employee:
  def __init__(self, e_id):
    self.id = e_id
    self.on_leave = false 
 
class SampleDatabaseLibrary:
  def __init__(src, dst, rel_name, card):
    self.src = src
    self.dst = dst
    self.rel_name = rel_name
    self.card = card
    # todo
    
  def add_operation(op):
    # todo
    return
  
  def add_assertion(ass):
    # todo
    return
    
  def select_one(tp, id):
    # todo
    return res
  
  def select_all(tp):
    #todo
    return res
  
  def select_associated(rel_name, obj):
    # todo
    return res
  
  def select_associated_inv(rel_name, obj):
    # todo
    return res
  
    
  
def emp_leave_req(db, emp_id):
  e = db.select_one(Employee, emp_id)
  tasks = db.select_associated("owns", e)
  for task in tasks:
    if (not task.is_done):
      return Error("Employee cannot go on leave. There are tasks to be done")
  e.on_leave = true
  return Success()
  
  
def mark_task_undone(db, task_id):
  t = db.select_one(Task, task_id)
  e = db.select_associated_inv("owns", t)
  if e.on_leave:
    return Error("Task cannot be marked as undone. The employee is on leave")
  t.is_done = false
  return Success()


def assert_invariant(db):
  # fetch all instances of Employee from the database
  emps = db.select_all(Employee)
  for emp in emps:
    if emp.on_leave:
      # For each employee on leave, make sure all of their tasks are done
      tasks = db.select_associated("owns",emp)
      for task in tasks:
        assert task.is_done
    
  
  
  
  if __name__ == "__main__":
    company_database = SampleDatabaseLibrary(Employee, Task, "owns","one_to_many");
    company_database.add_operation(emp_leave_req)
    company_database.add_operation(mark_task_undone)
    company_database.add_assertion(assert_invariant)
    
    verifier = Verifier()
    imps = get_candidate_implementations(company_database) # either user provides the implementation, or a synthesizer
    
    for imp in imps:
      res, cex = verifier.verify(company_database, imp)
      if res:
        print ("Implementation " + src(imp) + " is sound w.r.t. the specification of company_database")
      else:
        print ("Implementation " + src(imp) + " is unsound w.r.t. the specification of company_database")
        print ("Here is a counter example: \n" + src(cex))
    
    

  
  
  
  
