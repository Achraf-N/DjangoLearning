from rest_framework import permissions


class IsStuffEditorPermission(permissions.DjangoModelPermission):
  def has_permission(self,request,view):
    return True;

