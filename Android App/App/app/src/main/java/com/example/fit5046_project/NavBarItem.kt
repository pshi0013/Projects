package com.example.fit5046_project

import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.*
import androidx.compose.material.icons.rounded.Star
import androidx.compose.ui.graphics.vector.ImageVector

data class NavBarItem (
    val label : String = "",
    val icon : ImageVector = Icons.Filled.AccountCircle,
    val route : String = ""
){
    fun NavBarItems(): List<NavBarItem> {
        return listOf( NavBarItem(
            label = "Home",
            icon = Icons.Filled.Home,
            route = Routes.Home.value
        ),
            NavBarItem(
                label = "Profile",
                icon = Icons.Filled.AccountCircle, route = Routes.Profile.value
            ),

            NavBarItem(
                label = "Tracker",
                icon = Icons.Filled.Add, route = Routes.Tracker.value
            ),

            /*
            NavBarItem(
                label = "Food",
                icon = Icons.Filled.Create, route = Routes.Food.value
            ),
            NavBarItem(
                label = "Exercise",
                icon = Icons.Filled.Create, route = Routes.Exercise.value
            ),

             */
            NavBarItem(
                label = "Goal",
                icon = Icons.Rounded.Star, route = Routes.Goal.value
            ),
        )
    }
}