def role_required(role):
    def decorator(func):
        def wrapper(user_role, *args, **kwargs):
            if user_role != role:
                print(f"Access denied! Role '{role}' required.")
                return
            return func(user_role, *args, **kwargs)
        return wrapper
    return decorator

@role_required("admin")
def delete_user(user_role, username):
    print(f"User {username} deleted.")

delete_user("admin", "Alice")
delete_user("guest", "Bob")
