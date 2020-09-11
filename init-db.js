db.createUser(
    {
        user: "api_user",
        pwd: "api123",
        roles: [
            {
                role: "readWrite",
                db: "assessment"
            }
        ]
    })