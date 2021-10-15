package com.example.memebank

import android.app.VoiceInteractor
import android.content.Intent
import android.graphics.drawable.Drawable
import android.net.sip.SipSession
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.view.PixelCopy.request
import android.view.View
import android.widget.ImageView
import android.widget.ProgressBar
import android.widget.Toast
import com.android.volley.Request
import com.android.volley.Response
import com.android.volley.toolbox.JsonArrayRequest
import com.android.volley.toolbox.JsonObjectRequest
import com.android.volley.toolbox.StringRequest
import com.android.volley.toolbox.Volley
import com.bumptech.glide.Glide
import com.bumptech.glide.load.DataSource
import com.bumptech.glide.load.engine.GlideException
import com.bumptech.glide.request.RequestListener
import com.bumptech.glide.request.target.Target
import org.json.JSONObject

class MainActivity : AppCompatActivity() {

    var currMeme:String? = null
    override fun onCreate(savedInstanceState: Bundle?) {

        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        loadMeme()
    }

    fun loadMeme() {
//        var q = Volley.newRequestQueue(this)
        var url = "https://meme-api.herokuapp.com/gimme"
        val prg = findViewById<ProgressBar>(R.id.progBar)
        prg.visibility = View.VISIBLE
        var jsonObjectRequest = JsonObjectRequest(  Request.Method.GET, url, null,
            Response.Listener { response ->
                currMeme = response.getString("url")
                var memeImageView = findViewById<ImageView>(R.id.memeImageView)
                Glide.with(this).load(currMeme).listener(object :RequestListener<Drawable>{
                    override fun onLoadFailed(
                        e: GlideException?,
                        model: Any?,
                        target: Target<Drawable>?,
                        isFirstResource: Boolean
                    ): Boolean {
                        prg.visibility = View.GONE
                        return false
                    }

                    override fun onResourceReady(
                        resource: Drawable?,
                        model: Any?,
                        target: Target<Drawable>?,
                        dataSource: DataSource?,
                        isFirstResource: Boolean
                    ): Boolean {
                        prg.visibility = View.GONE
                        return false
                    }
                }) .into(memeImageView)
            },
            Response.ErrorListener {
                Toast.makeText(this, "Something went wrong!", Toast.LENGTH_SHORT).show()
            })
//        q.add(jsonObjectRequest)
        MySingleton.getInstance(this).addToRequestQueue(jsonObjectRequest)
    }



    public fun shareMeme(v: View) {
        val intent = Intent(Intent.ACTION_SEND)
        intent.type = "text/plain"
        intent.putExtra(Intent.EXTRA_TEXT,"Reddit Meme Delicacy..!!! \n $currMeme")
        val chooser = Intent.createChooser(intent,"Wish to Share....")
        startActivity(chooser)
    }
    public fun nextMeme(v: View) {
        loadMeme()
    }
}



