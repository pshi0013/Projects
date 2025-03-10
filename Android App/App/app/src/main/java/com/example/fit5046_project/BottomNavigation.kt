package com.example.fit5046_project

import androidx.compose.foundation.layout.padding
import androidx.compose.material.BottomNavigation
import androidx.compose.material.BottomNavigationItem
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Delete
import androidx.compose.material.icons.filled.Home
import androidx.compose.material3.Icon
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.navigation.NavDestination.Companion.hierarchy
import androidx.navigation.NavGraph.Companion.findStartDestination
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.compose.currentBackStackEntryAsState
import androidx.navigation.compose.rememberNavController

@Composable
fun BottomNavigationBar() {
    val navController = rememberNavController()
    Scaffold(
        bottomBar = {
            BottomNavigation (backgroundColor= Color.LightGray ){
                val navBackStackEntry by
                navController.currentBackStackEntryAsState()
                val currentDestination = navBackStackEntry?.destination

                NavBarItem().NavBarItems().forEach { navItem ->
                    BottomNavigationItem(
                        icon = { Icon(navItem.icon, contentDescription = null) },
                        label = { Text(navItem.label) },
                        selected = currentDestination?.hierarchy?.any {
                                it.route == navItem.route } == true,
                        onClick = { navController.navigate(navItem.route) {
                            popUpTo(navController.graph.findStartDestination().id) {
                                saveState = true
                            }
                            launchSingleTop = true
                            restoreState = true
                        }
                        }
                    )
                } }
        }
    ) { paddingValues ->
        NavHost(
            navController,
            startDestination = Routes.Home.value,
            Modifier.padding(paddingValues) ){
            composable(Routes.Home.value) {
                Home(navController)
            }
            composable(Routes.Profile.value) {
                Profile(navController) }

            composable(Routes.Tracker.value) {
                Profile(navController) }
            /*
            composable(Routes.Food.value) {
                Food(navController)}
            composable(Routes.Exercise.value) {
                Exercise(navController)}

             */
            composable(Routes.Goal.value) {
                Goal(navController)
            }
        }
    }
}
