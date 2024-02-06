
def register_user():
	new_user1= input('Enter your first name:')
	new_user2= input('Enter your last name:')
	user_email = f'{new_user1}.{new_user2}@email.com'
	full_name = f'{new_user1} {new_user2}'
	created_user = {'user_name':full_name, 'email': user_email}


	print(f'Welcome {new_user1} {new_user2} Your email is {user_email} ')

	return created_user

def edit_user(user):
	new_name= input('Enter your first name:')
	new_name2= input('Enter your last name:')
	new_email = f'{new_name}.{new_name2}@email.com'
	new_full = f'{new_name} {new_name2}'
	new_created = {'user_name': new_full, 'email': new_email}

	print(f'Your new name is {new_full}')
	return new_created



