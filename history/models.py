from django.db import models
from users.models import User
from branches.models import Branch

class History(models.Model):
   client_id = models.ForeignKey(User, on_delete=models.SET_DEFAULT, related_name="client_id", null=True, blank=True, default=None)
   employee_id = models.ForeignKey(User, on_delete=models.SET_DEFAULT, related_name="employee_id", null=True, blank=True, default=None)
   branch_id = models.ForeignKey(Branch, on_delete=models.SET_DEFAULT, related_name="branch_id", null=True, blank=True, default=None)
   check_in_time = models.DateTimeField(auto_now_add=True)
   check_out_time = models.DateTimeField(null=True, blank=True)
   payment = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

   def __str__(self):
      return f"{self.client.first_name} -> {self.check_in_time.strftime('%Y-%m-%d %H:%M:%S')}"
   
