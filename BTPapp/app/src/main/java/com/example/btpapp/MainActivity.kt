package com.example.btpapp

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.*
import androidx.compose.material.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.sp
import com.android.volley.Request
import com.android.volley.RequestQueue
import com.android.volley.toolbox.JsonObjectRequest
import com.android.volley.toolbox.StringRequest
import com.android.volley.toolbox.Volley
import com.example.btpapp.ui.theme.BTPappTheme

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        val queue = Volley.newRequestQueue(this)
        setContent {
            Column(modifier = Modifier
                .fillMaxWidth()
                .fillMaxHeight(0.67f),
                horizontalAlignment = Alignment.CenterHorizontally,
                verticalArrangement = Arrangement.SpaceEvenly
            ) {
                Text(text = "BTPapp", fontWeight = FontWeight.ExtraBold, fontSize = 30.sp)

                Text(text = "Add/Remove RFID code", fontWeight = FontWeight.ExtraBold, fontSize = 15.sp)

                var text by remember { mutableStateOf("") }

                TextField(value = text, onValueChange = { newText -> text = newText})
                
                Row(modifier = Modifier.fillMaxWidth(),
                    horizontalArrangement = Arrangement.SpaceEvenly,
                    verticalAlignment = Alignment.CenterVertically
                ) {
                    Button(onClick = { grantAccess(text, queue) }) {
                        Text(text = "Add id")
                    }
                    
                    Button(onClick = { revokeAccess(text, queue) }) {
                        Text(text = "Remove id")
                    }
                }

                Text(text = "Set Temperature", fontWeight = FontWeight.ExtraBold, fontSize = 15.sp)

                var temp by remember { mutableStateOf("") }

                TextField(value = temp, onValueChange = { newText -> temp = newText})

                Button(onClick = { /*TODO*/ }) {
                    Text(text = "Set Temperature")
                }
            }
        }
    }

    private fun grantAccess(id: String, queue: RequestQueue) {
        val url = "https://BTP.pranavraj14.repl.co/grant_access/$id"

        val stringObjectRequest = StringRequest(
            Request.Method.POST, url, null, null
        )

        queue.add(stringObjectRequest)
    }

    private fun revokeAccess(id: String, queue: RequestQueue) {
        val url = "https://BTP.pranavraj14.repl.co/revoke_access/$id"

        val stringObjectRequest = StringRequest(
            Request.Method.PUT, url, null, null
        )

        queue.add(stringObjectRequest)
    }
}

@Composable
fun Greeting(name: String) {

}

@Preview(showBackground = true)
@Composable
fun DefaultPreview() {

}