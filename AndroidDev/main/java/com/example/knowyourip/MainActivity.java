package com.example.knowyourip;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.ListView;
import android.widget.TextView;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {

    // CALL-OFFS
    Button get_ip_button;
    TextView textView;
    RequestQueue queue;
    String tempIP;
    ArrayList arr;
    ListView lmp;

    // TO GET THE IP ADDRESS
    public void jsonParse(){
        String url ="https://api.ipify.org?format=json";
        JsonObjectRequest request = new JsonObjectRequest(Request.Method.GET, url, null,
                new Response.Listener<JSONObject>() {
                    @Override
                    public void onResponse(JSONObject response) {
                        try {
                            String s = response.getString("ip");
                            textView.setText(s);
                            tempIP = s;
                        } catch (JSONException e) {
                            e.printStackTrace();
                            textView.setText("That Didn't Work !!");
                        }
                    }
                },
                new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {
                        textView.setText("That Didn't Work !!");
                    }
                });
        queue.add(request);
    }

    // TO GET OTHER INFO FROM CALLED IP
    public void jsonParse2()
    {
        Log.d("myres", "jsonParse2: "+tempIP);
        String url ="https://ipinfo.io/" + (String) tempIP + "/geo";

        JsonObjectRequest request = new JsonObjectRequest(Request.Method.GET, url, null,
                new Response.Listener<JSONObject>() {
                    @Override
                    public void onResponse(JSONObject response) {
                        try {
                            String s;
                            s = response.getString("city");
                            arr.add((String)("Your City : " + (String)s));
                            s = response.getString("region");
                            arr.add((String) ("Rgion you live in : " +  (String)s));
                            s = response.getString("country");
                            arr.add((String)("Country : " +  (String)s));
                            s = response.getString("loc");
                            arr.add((String)("Location : " +  (String)s));
                            s = response.getString("org");
                            arr.add((String)("Org : " +  (String)s));
                            s = response.getString("postal");
                            arr.add((String)("Postal : " +  (String)s));
                            s = response.getString("timezone");
                            arr.add((String)("TimeZone : " + (String)s));
                            setList();
                        } catch (JSONException e) {
                            e.printStackTrace();
                            textView.setText("That Didn't Work !!");
                        }
                    }
                },
                new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {
                        textView.setText("That Didn't Work !!");
                    }
                });
        Log.d("myres", "jsonParse2: "+tempIP + " and size of arr : " + String.valueOf(arr.size()));
        queue.add(request);

        // AFTER REQUEST QUEUED, DELETE THE ARRAYLIST SO AFTER NEW PRESSES LIST DOESNT GET A "ADD ON" AGIN AND AGAIN
        clrList();
    }

    // FOR SETTING ARRAYLIST TO LISTVIEW
    public void setList(){
        Log.d("myres", "setList: ");
        Log.d("myres", String.valueOf(arr.size()));
        ArrayAdapter<String> arrAdadpter = new ArrayAdapter<String>(MainActivity.this,android.R.layout.simple_list_item_1, arr);
        lmp.setAdapter(arrAdadpter);
    }

    // TO CLEAR ARRAYLIST
    public void clrList(){
        Log.d("myres", "clrList: ");
        arr.clear();
    }

    // ONCREATE
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        textView = (TextView) findViewById(R.id.responseTextview);
        get_ip_button = findViewById(R.id.GetIPButton);
        queue = Volley.newRequestQueue(this);

        lmp = findViewById(R.id.dynamiclist);
        arr = new ArrayList<String>();

        get_ip_button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                jsonParse();
                jsonParse2();
            }
        });
    }

}